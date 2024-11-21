from binance.client import Client
import requests

# 替换为你的API密钥和密钥
api_key = ''
api_secret = ''

# 设置 SOCKS5 代理
proxies = {
    'http': 'socks5h://ip:port',
    'https': 'socks5h://ip:port',
}

# 创建客户端
client = Client(api_key, api_secret)

# 替换默认的 session 对象，设置代理
client.session = requests.Session()
client.session.proxies.update(proxies)

# 查询账户信息
def get_account_balances():
    try:
        account_info = client.get_account()
        balances = account_info['balances']
        
        # 筛选余额大于0的币种
        active_balances = [
            {'asset': balance['asset'], 'free': balance['free'], 'locked': balance['locked']}
            for balance in balances if float(balance['free']) > 0 or float(balance['locked']) > 0
        ]

        # 打印结果
        for balance in active_balances:
            print(f"Asset: {balance['asset']}, Free: {balance['free']}, Locked: {balance['locked']}")

    except Exception as e:
        print(f"Error: {e}")

get_account_balances()
