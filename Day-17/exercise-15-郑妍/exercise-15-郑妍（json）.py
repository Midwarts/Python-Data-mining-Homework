import json,MySQLdb

def add_json(): 
    try:
        con = MySQLdb.Connect(
            host='mysql服务器地址',
            user='用户名',passwd='密码',
            db='数据库名称',port=3306,
            charset = 'utf8'
            ) 
        cur = con.cursor()
        sql = "SELECT id, 姓名, 出生日期, 年龄, 性别 FROM exercise-15-郑妍"
        cur.execute(sql)
        data = cur.fetchall()

        json_data = []
        for row in data:  
            result = {} 
            result['id'] = str(row[0])  
            result['姓名'] = str(row[1])  
            result['出生日期'] = str(row[2])  
            result['年龄'] = str(row[3])   
            result['性别'] = str(row[4])  
            jsonData.append(result)
            
    except:  
        print( 'MySQL connect fail.')  
    else:
        json=json.dumps(jsonData,ensure_ascii = False)
        return json[1:len(json)-1]
  
if __name__ == '__main__':  
    json_data = add_json() 
    f = open(r'exercise-15-郑妍.json','w+')
    f.write(json_data)
