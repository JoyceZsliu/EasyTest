"""
 * @description: TODO 
 * @author ChenDong
 * @date 2024/8/19 下午5:10
 * @version 1.0
"""
from testTools.common.makeTestCases.caseTools import dataMaker
from testTools.common.save import save

make = dataMaker()
file = 'Cases.csv'
save(file, make.equalsMake())

"""
查询成功
查询失败
3
手机号
正确 1 2
错误 空
姓名
正确 4 2
错误 空
时间
正确 4 5
错误 空


"""