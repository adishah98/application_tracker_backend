from project import db
from project.com.vo.AppliedJobsVo import AppliedJobsVo

pstvo=AppliedJobsVo()
class AppliedJobsDAO:
    def addAppliedJob(self, AppliedJobsVo):
        db.session.add(AppliedJobsVo)
        db.session.commit()

    def getAllAppliedJob(self):
        appliedJobs=AppliedJobsVo.query.all()
        print('group dao',appliedJobs)
        return appliedJobs
    
    def getAppliedJobById(self,obj):
        job=AppliedJobsVo.query.filter_by(applicationId = obj).all()
        return job[0]

    def updateAppliedJob(self, AppliedJobsVo):
        db.session.update(AppliedJobsVo)
        db.session.commit()


    def deleteAppliedJob(self, ApplicationId):
        job=self.getAppliedJobById(ApplicationId)
        db.session.delete(job)
        db.session.commit()
        return 