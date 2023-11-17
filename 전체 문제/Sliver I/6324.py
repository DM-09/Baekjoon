for i in range(int(input())):
    inp = input().split('://')
    host = "://".join(inp[1:]).split('/')

    port = host[0].split(':')[1] if host[0].count(':') else '<default>'

    if i: print()

    print(f'URL #{i + 1}')
    print(f'Protocol = {inp[0]}')
    print(f'Host     = {host[0].split(":")[0]}')
    print(f'Port     = {port}')
    print(f'Path     = {"/".join(host[1:]) if len(host) != 1 else "<default>"}')
