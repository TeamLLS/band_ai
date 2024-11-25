class PayBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # 상태: open, close 등
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class PayMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pay_book_id = db.Column(db.Integer, db.ForeignKey('pay_book.id'), nullable=False)
    member_id = db.Column(db.Integer, nullable=False)
    amount_paid = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # 납부 상태: paid, unpaid 등
