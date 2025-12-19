from .client import Client

client = Client("username", "api_key", "api_password", demo=True)

account = client.all_accounts()["accounts"]

client.change_active_account(account[0]["accountId"])

deal_id = client.create_position("TSLA", "BUY", 5)

positions = client.all_positions()


client.update_position(deal_id=deal_id["affectedDeals"][0]["dealId"])

print(
    f"I´ve made {client.close_position(deal_id=deal_id['affectedDeals'][0]['dealId'])['profit']}$ of profit!"
)
