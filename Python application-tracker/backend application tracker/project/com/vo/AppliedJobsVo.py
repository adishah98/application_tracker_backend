from project import db
from project import app

class AppliedJobsVo(db.Model):
    __tablename__ = 'AppliedJobs'
    applicationId=db.Column('ApplicationId',db.Integer, primary_key = True)
    companyName = db.Column('companyName',db.String(100))
    url=db.Column('url',db.Integer)
    date=db.Column('applied_on',db.DateTime(timezone=True))
    status=db.Column('status',db.Integer)
    position=db.Column('position',db.Integer)

    def to_dict(self):
        return {
        'Company': self.companyName,
        'Location': self.status,
        "URL": self.url,
        "Postion":  self.position,
        "Status":self.status,
        "ApplicationId":self.applicationId
        }
with app.app_context():
    db.create_all()


