#BMI= 体重 /（身高**2）
user_weight = float(input("请输入您的体重(单位：kg)："))
user_height = float(input("请输入您的身高(单位：50m)："))
user_BMI = user_weight/user_height**2
print("您的BMI值为：",user_BMI)

#我国成人BMI分类以 BMI=体重 (kg)/身高² (m²) 为计算方式，将体重分为四类：
# 偏瘦（BMI<18.5）
# 正常（18.5≤BMI<24）
# 超重（24≤BMI<28）
# 肥胖（BMI≥28）
if user_BMI <= 18.5:
    print("此BMI值属于偏瘦范围。")
elif 18.5< user_BMI <= 24:
    print("此BMI值属于正常范围。")
elif 24 < user_BMI <= 28:
    print("此BMI值属于偏胖范围。")
else:
    print("此BMI值属于肥胖范围。")