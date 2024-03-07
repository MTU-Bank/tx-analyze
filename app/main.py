import uvicorn
from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from app.model.model import get_predict

app = FastAPI()


class In(BaseModel):
    step: int
    amount: float
    oldBalanceOrig: float
    newBalanceOrig: float
    oldBalanceDes: float
    newBalanceDes: float
    CASH_OUT: int  # [0, 1]
    DEBIT: int  # [0, 1]
    PAYMENT: int    # [0, 1]
    TRANSFER: int   # [0, 1]


@app.get('/')
def home():
    return 'Ok'


@app.post('/predict')
def predicted(features: Annotated[In, Depends()]):
    result = get_predict([
        features.step,
        features.amount,
        features.oldBalanceOrig,
        features.newBalanceOrig,
        features.oldBalanceDes,
        features.newBalanceDes,
        features.CASH_OUT,
        features.DEBIT,
        features.PAYMENT,
        features.TRANSFER])
    return {'result': result}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
