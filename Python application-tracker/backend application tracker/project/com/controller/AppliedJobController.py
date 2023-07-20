from project import app
from flask import request, jsonify
from project.com.dao.AppliedJobsDAO import AppliedJobsDAO
from project.com.vo.AppliedJobsVo import AppliedJobsVo
import json


dao=AppliedJobsDAO()

@app.route('/add-appliedjob',methods=['POST'])
def addAppliedJob():
    print('received request....................')
    data = json.loads(request.data)
    vo=AppliedJobsVo()
    vo.companyName=data['Company']
    vo.position=data['Postion']
    vo.status=data['Status']
    vo.url=data['URL']
    dao.addAppliedJob(vo)
    appliedJobs=dao.getAllAppliedJob()
    data=[]
    for i in appliedJobs:
        data.append(i.to_dict())
    return jsonify(data)

@app.route('/get-appliedjob',methods=['get'])
def getAllAppliedJob():
    print('inside get all applied jobs')
    appliedJobs=dao.getAllAppliedJob()
    print('all the jobs are fetched')
    data=[]
    for i in appliedJobs:
        data.append(i.to_dict())
    return jsonify(data)


@app.route('/update-appliedjob',methods=['POST'])
def updateAppliedJob():
    data = json.loads(request.data)
    newObj=AppliedJobsVo()
    print()
    newObj.applicationId=data['ApplicationId']
    print(newObj.applicationId)
    print(type(newObj.applicationId))

    print("inside update jon controller")

    oldObj=dao.getAppliedJobById(newObj.applicationId)
    oldObj.companyName=data['Company']
    oldObj.position=data['Postion']
    oldObj.status=data['Status']
    oldObj.url=data['URL']
    dao.addAppliedJob(oldObj)
    appliedJobs=dao.getAllAppliedJob()
    data=[]
    for i in appliedJobs:
        data.append(i.to_dict())
    return jsonify(data)


@app.route('/delete-appliedjob',methods=['POST'])
def deleteAppliedJobData():
    data = json.loads(request.data)
    obj=AppliedJobsVo()
    print()
    obj.applicationId=data['ApplicationId']
    dao.deleteAppliedJob(obj.applicationId)
    appliedJobs=dao.getAllAppliedJob()
    data=[]
    for i in appliedJobs:
        data.append(i.to_dict())
    return jsonify(data)


@app.route('/get',methods=['get'])
def getData():

    appliedJobs=dao.getAllAppliedJob()
    data=[]
    for i in appliedJobs:
        data.append(i.to_dict())
    return jsonify(data)
