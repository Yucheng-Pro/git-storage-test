#Yucheng_repository
#实习-IPO审计-一致性核查
import pandas as pd
# 读取采购-抽凭-细节测试环节数据
contracts = pd.read_excel('采购合同.xlsx')
receipt_storage = pd.read_csv('入库凭证.csv')
# 筛选字段匹配（合同编号后6位+物料信息-金额 ）
contracts['short_id'] = contracts['合同编号'].str[-6:]
receipt_storage['short_id'] = receipt_storage['备注'].str.extract(r'(\d{6})$')
# 左连接匹配
matched = pd.merge(contracts, receipt_storage, on=['short_id','入库物料金额'], how='left')
# 输出未匹配数据转待复核
unmatched = matched[matched['入库单编号'].isnull()]
unmatched.to_excel('待复核数据表.xlsx')