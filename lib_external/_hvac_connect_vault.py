import hvac
import sys

# python hvac包 调用 vault 存取密钥/获取PKI证书


# Authentication
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='hvs.rZBLPYkkyPQ4oTRJsQMZrYKf',
)


def basic_info():
    is_authenticated = client.is_authenticated()
    is_initialized = client.sys.is_initialized()
    is_sealed = client.sys.is_sealed()

    # unseal
    client.sys.submit_unseal_key('')
    client.sys.submit_unseal_keys([])


def kv_demo():

    # Writing a secret
    # http://127.0.0.1:8200/v1/kv/data/secret/fee
    create_response = client.secrets.kv.v2.create_or_update_secret(
        path='foo',
        mount_point='kv',        # k-v engine 的path name, 默认secret
        secret=dict(password='Hashi123456'),
    )
    print('Secret written successfully.')

    # Reading a secret
    read_response = client.secrets.kv.read_secret_version(
        path='foo',
        mount_point='kv',
    )
    print('read_response ---->  ', read_response)

    password = read_response['data']['data']['password']
    if password != 'Hashi123456':
        sys.exit('unexpected password')

    print('Access granted!')


def pki_demo():
    """
    pki doc: https://hvac.readthedocs.io/en/stable/usage/secrets_engines/pki.html
    :return:
    """
    # Read CA Certificate
    # read_ca_certificate_response = client.secrets.pki.read_ca_certificate(mount_point='pki-root')
    read_ca_certificate_response = client.secrets.pki.read_ca_certificate(mount_point='pki-mid')
    print(read_ca_certificate_response)

    # Read CA Certificate Chain
    # read_ca_certificate_chain_response = client.secrets.pki.read_ca_certificate_chain(mount_point='pki-mid')
    # print(read_ca_certificate_chain_response)

    # Read Certificate
    # read_certificate_response = client.secrets.pki.read_certificate(serial='crl', mount_point='pki-mid')
    # print(read_certificate_response)
    # print(read_certificate_response['data']['certificate'])

    # list_certificate_response = client.secrets.pki.list_certificates(mount_point='pki-mid')
    # print(list_certificate_response)
    # print(list_certificate_response['data']['keys'])

    # Generate Intermediate
    # generate_intermediate_response = client.secrets.pki.generate_intermediate(
    #     type='exported',
    #     common_name='example.com',
    #     mount_point='pki-hehe',
    # )
    # print('Intermediate certificate: {}'.format(generate_intermediate_response))

def save_ca(filename, data):
    with open('./generate_cert/' + filename, 'w') as f:
        f.write(data)

def pki_generate_ca():
    root_path = 'pki-r1'
    mid_path = 'pki-m1'
    domain = '127.0.0.1'

    # enable secret engine for root
    client.sys.enable_secrets_engine(
        backend_type='pki',
        path=root_path,
        config={
            'default_lease_ttl': 36500,
            'max_lease_ttl': 36500
        }
    )
    print('-------- enable secret engine for root --------')

    # generate root  URLS和CRL以后可以根据需求自己更改 ; CA type为root
    generate_root_response = client.secrets.pki.generate_root(
        type='internal',
        common_name=domain,
        mount_point=root_path,
        extra_params={'ttl': '36499'},
    )
    # print('generate root response ---->  ', generate_root_response)
    root_ca = generate_root_response['data']['certificate']
    print('root certificate ---->  ', root_ca)
    save_ca('root_ca.pem', root_ca)

    # enable secret engine for mid
    client.sys.enable_secrets_engine(
        backend_type='pki',
        path=mid_path,
        config={
            'default_lease_ttl': 36499,
            'max_lease_ttl': 36499
        }
    )
    print('-------- enable secret engine for mid --------')

    # generate intermediate 生成CSR； CA type为Intermediate
    generate_intermediate_response = client.secrets.pki.generate_intermediate(
        type='internal',
        common_name=domain,
        mount_point=mid_path
    )
    print('generate_intermediate_response ---->  ', generate_intermediate_response)
    CSR = generate_intermediate_response['data']['csr']
    print('CSR ---->  ', CSR)

    # sign intermediate 将CSR交给root进行签名
    # CSR = '-----BEGIN CERTIFICATE REQUEST-----\nMIIChDCCAWwCAQAwFjEUMBIGA1UEAxMLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3\nDQEBAQUAA4IBDwAwggEKAoIBAQC0xGT5HDtzlcL9ytUrTYN8Az7v6h/bLfvijBpD\nisDvE/QTWtIY6v9J+zveYhkL2FMYGjKWZtj8ZM6i6bbk8Ztt688fmvUFQimqbFOM\nBpLJy/cxlNrr+xi55mDx5upJmoeAuK5QiQ1EqWoSN9P6hqbta/rE4HmI3u/tMhST\n/5McR+UtG4filPQiOGtdKi19+o9c9XTEns5y5q6Oxxbg7op/sCopuUOnKG/Ftlms\nwMEDLHR0xgBi9tBDhAI1hKuO2lKLNX1bwvvzZXli9Y3u0rChg3mbqjxr92T4zuVb\nBqNMmMVo+TUeIg0DuItoxnTfIn3vtvEA5iJ+e40pSA2uEX+hAgMBAAGgKTAnBgkq\nhkiG9w0BCQ4xGjAYMBYGA1UdEQQPMA2CC2V4YW1wbGUuY29tMA0GCSqGSIb3DQEB\nCwUAA4IBAQAO/aIRonYdVeXAlg1Vl7etso0HO3p7MwTjET6Ke0eWjkiXzsrz5YFU\nvO8BUIZHzmUEvVpLngN1G8cO81rBNAboIC0kblyg67dBRpzyPUPJIiLCdcmL3LRz\nTTFDqm+nhYhD7u+hb93UbjyqNy+I5ZrUEfQby0M7E2+V2lKljfp2g7h//NpbR6ck\nKQ656tP79KHWCpgffVrWJXwr79oMhkCcNl7vBFiGABXjBe4IO1WY1/1HV4ZRNOY2\nHgONIQZ21FYLtt51rv5qdk4zsxXzajOxtmbNphc7xDMEyhYsu0FceFCVPq7a0LG+\ns0TY2aj3LCthvzTwpzJYfnCLGkIdl4GE\n-----END CERTIFICATE REQUEST-----'
    sign_intermediate_response = client.secrets.pki.sign_intermediate(
        csr=CSR,
        common_name=domain,
        mount_point=root_path,
        extra_params={'ttl': '36499'}        # ttl等
    )
    print('Signed certificate response ---->  ', sign_intermediate_response)
    print('-------- 成功签发中间证书 --------')
    certificate = sign_intermediate_response['data']['certificate']
    # certificate = '-----BEGIN CERTIFICATE-----\nMIIDNTCCAh2gAwIBAgIUfZ6Oja/Wz/pfYLLpLhQjxAgLxzMwDQYJKoZIhvcNAQEL\nBQAwFjEUMBIGA1UEAxMLZXhhbXBsZS5jb20wHhcNMjIwNjE1MDIyODA5WhcNMjIw\nNjE1MTIzNjU5WjAWMRQwEgYDVQQDEwtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcN\nAQEBBQADggEPADCCAQoCggEBALTEZPkcO3OVwv3K1StNg3wDPu/qH9st++KMGkOK\nwO8T9BNa0hjq/0n7O95iGQvYUxgaMpZm2PxkzqLptuTxm23rzx+a9QVCKapsU4wG\nksnL9zGU2uv7GLnmYPHm6kmah4C4rlCJDUSpahI30/qGpu1r+sTgeYje7+0yFJP/\nkxxH5S0bh+KU9CI4a10qLX36j1z1dMSeznLmro7HFuDuin+wKim5Q6cob8W2WazA\nwQMsdHTGAGL20EOEAjWEq47aUos1fVvC+/NleWL1je7SsKGDeZuqPGv3ZPjO5VsG\no0yYxWj5NR4iDQO4i2jGdN8ife+28QDmIn57jSlIDa4Rf6ECAwEAAaN7MHkwDgYD\nVR0PAQH/BAQDAgEGMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFHIBcAfO2UTj\nQlnVBA/9LnOkw9yEMB8GA1UdIwQYMBaAFKFp6j2/6ygv938UXdj8u35l+W7EMBYG\nA1UdEQQPMA2CC2V4YW1wbGUuY29tMA0GCSqGSIb3DQEBCwUAA4IBAQB/KGBp5dTM\ngeLUMuLqmj33NrzcIxfYqeb+eXurmxcxVJrQjy8qG/JNUzrIgCWaIrV3E/8MOwi4\np8qF217BVyX3438USnTxHsmjloLHq4UyDId5fdU6v7XaqUP9mal2B+7d/OFSTKTW\npkUsj9VaQQ+YzO29lIf6w0S/UXQTL9derJcjn4obA3sM4JjRYXdXtVeWmU1SNrHX\na8stFlAbltDR52oWd9wAVQYaOMjcHvy9bcmFtx4nmkrBu4FoYniEmUO/VewJwZv2\nLO/OItJfboiXff1nUqbtNnwId+DaCJkcq5uwbjtuDdDhuB972/hrCqS+1KRdt+/j\nw/RA265evYxr\n-----END CERTIFICATE-----'
    # issuing_ca = sign_intermediate_response['data']['issuing_ca']      # 签发的CA，即根CA
    # issuing_ca = '-----BEGIN CERTIFICATE-----\nMIIDNTCCAh2gAwIBAgIUAWkWjVApKXitrUMpBhe/l9JBmTYwDQYJKoZIhvcNAQEL\nBQAwFjEUMBIGA1UEAxMLZXhhbXBsZS5jb20wHhcNMjIwNjE1MDIwODA4WhcNMjIw\nNjE1MTIxNjU4WjAWMRQwEgYDVQQDEwtleGFtcGxlLmNvbTCCASIwDQYJKoZIhvcN\nAQEBBQADggEPADCCAQoCggEBAOc1OfjgKMtFU/PBYmTSYnyuFLptiKMj1akWVQkZ\nvCiOV4/2FE8j/379o6UbsolkoLOdUeURjfciPBwzrQeTNoFLSDjLs5Ec5qzCJXSI\n173UzNqDNfst565q051HbSbOnY63c888NEp8LcaKp9X1deu8UIt2dOHHFZ3xPbqG\npPCDjhRGGG2i4GvYHji1W68DYmCZcAQdoxQpUcO5dyuimr/2f6Ghm0R/rs1Vh2ma\nPXYk304QKA/aQJiFpXJibAk1geTnVEfvwpNZpKA8cXnw5t/8y6/ZrhVK+JYxjG7Z\niZaSnoZ0da2WJtO0GH5KwO3V5E3FJjMSU+rqwyEaphQqgEcCAwEAAaN7MHkwDgYD\nVR0PAQH/BAQDAgEGMA8GA1UdEwEB/wQFMAMBAf8wHQYDVR0OBBYEFKFp6j2/6ygv\n938UXdj8u35l+W7EMB8GA1UdIwQYMBaAFKFp6j2/6ygv938UXdj8u35l+W7EMBYG\nA1UdEQQPMA2CC2V4YW1wbGUuY29tMA0GCSqGSIb3DQEBCwUAA4IBAQAm/n/PJ8Eb\nD7ddoi2MJZ1JOQ46+5vXDMK1gE8FT7RsqmXucJVpn16MIvpKVNg0wm96nx9BoNnl\nd6D7pWYW94YBOVNZj6K/1vyXjAnG0cfOcR1PSGEN8VSNdrkuVPssfAWHi+Wrn7YY\nL95Vh0s6FYp9F5/91WtAH0/9NdDnzzvZGvtS0ac7RyjnoLCVBnud4PYEoj6+qvqr\nALad+COru5OHU9PLczaZx2ps0yRibr7OgcIWttOVLoAceq0OUyEP/Qmwm6uBSnL5\nJn05xklHVnCmCzQ6ksyVstDSN7I65l7Z94VNojO+//ceISATD33VqqxpJWGlUkS1\n4OveMYy1ZwWX\n-----END CERTIFICATE-----'
    print('mid certificate ---->  ', certificate)
    save_ca('mid_ca.pem', certificate)

    # set signed intermediate     已被root签名的中间证书保存到pki-m里
    set_signed_intermediate_response = client.secrets.pki.set_signed_intermediate(
        certificate=certificate,             # CSR 中的 certificate
        mount_point=mid_path
    )
    print('set_signed_intermediate_response ---->  ', set_signed_intermediate_response)     # <Response [204]>

    # pki-m 里创建 role
    create_or_update_role_response = client.secrets.pki.create_or_update_role(
        'role-name',
        extra_params={
            'ttl': '34999',
            'max_ttl': '34999',
            'allow_localhost': True,
            'allow_bare_domains': True,
            'allow_subdomains': True,
            'allow_glob_domains': True,
            'allow_any_name': True,
            'enforce_hostnames': True,
            'allow_ip_sans': True,
            'use_csr_common_name': True,
            'use_csr_sans': True,
        },
        mount_point=mid_path
    )
    print('New role: {}'.format(create_or_update_role_response))    # <Response [204]>

    # 根据这个role生成最终用户ca证书
    # generate certificate
    generate_certificate_response = client.secrets.pki.generate_certificate(
        name='role-name',
        common_name=domain,
        mount_point=mid_path,
        extra_params={'ttl': '34998'},
    )
    # print('generate_certificate_response ---->  ', generate_certificate_response)
    print('ca_chain_list ---->  ', generate_certificate_response['data']['ca_chain'])
    print('issuing_ca 即 mid CA ---->  ', generate_certificate_response['data']['issuing_ca'])
    user_cert = generate_certificate_response['data']['certificate']
    print('user certificate ---->  ', user_cert)
    save_ca('user_cert.pem', user_cert)
    u_private_key = generate_certificate_response['data']['private_key']
    print('private_key ---->  ', u_private_key)
    save_ca('u_private.key', u_private_key)



if __name__ == '__main__':
    # kv_demo()
    # pki_demo()
    pki_generate_ca()






