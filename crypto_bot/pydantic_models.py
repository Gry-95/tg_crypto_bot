import pydantic
from datetime import datetime


class User(pydantic.BaseModel):
    id: int
    tg_ID: int
    nick: str = None
    create_date: datetime
    wallet: 'Wallet'
    sended_transactions: list['Transaction'] = None
    received_transactions: list['Transaction'] = None


class Transaction(pydantic.BaseModel):
    id: int
    sender: User = None
    receiver: User = None
    sender_wallet: 'Wallet' = None
    receiver_wallet: 'Wallet' = None
    sender_address: str
    receiver_address: str
    amount_btc_with_fee: float
    amount_btc_without_fee: float
    fee: float
    date_of_transaction: datetime
    tx_hash: str


class Wallet(pydantic.BaseModel):
    id: int
    user: User
    balance: float = 0.0
    private_key: str
    address: str
    sended_transactions: list[Transaction] = []
    received_transactions: list[Transaction] = []



class User_to_update(pydantic.BaseModel):
    id: int
    tg_ID: int = None
    nick: str = None
    create_date: datetime = None
    wallet: 'Wallet' = None


class User_to_create(pydantic.BaseModel):
    tg_ID: int = None
    nick: str = None


class Token(pydantic.BaseModel):
    access_token: str
    token_type: str


class TokenData(pydantic.BaseModel):
    username: str | None = None


class Admin(pydantic.BaseModel):
    username: str


class UserInDB(Admin):
    hashed_password: str


User_to_update.update_forward_refs()
User.update_forward_refs()
User_to_create.update_forward_refs()
Transaction.update_forward_refs()
Wallet.update_forward_refs()
