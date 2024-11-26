while True:
    try:
        print('---โปรแกรมหาพื้นที่ 4 เหลี่ยม---')
        a = int(input('ใส่ค่าความยาว: '))
        b = int(input('ใส่ค่าความกว้าง: '))
        
        if a == 0 or b == 0:
           raise ZeroDivisionError    
        elif a < 0 or b <0:
            raise Exception
        g = a * b
        print(f'พื้นที่ 4 เหลี่ยมคือ: {g}')
              
        print('---โปรแกรมหาพื้นที่ 3 เหลี่ยม---')
        a = int(input('ใส่ค่าความความสูง: '))
        b = int(input('ใส่ค่าความความยาวของฐาน: '))
        
        if a == 0 or b == 0:
           raise ZeroDivisionError    
        elif a < 0 or b <0:
            raise Exception
        g = 1.2*a * b
        print(f'พื้นที่ 3 เหลี่ยมคือ: {g}')

        print('---โปรแกรมหาพื้นที่วงกลม---')
        a = int(input('ใส่ค่ารัศมีของวงกลม: '))
        
        if a == 0 :
           raise ZeroDivisionError    
        elif a < 0 or b <0:
            raise Exception
        g = 3.14 * a**2
        print(f'พื้นที่วงกลมคือ: {g}')
    
    except ValueError:
        print('ใส่เฉพาะตัวเลข')
    except ZeroDivisionError:
        print('ห้ามใส่ค่าเป็น 0')
    except :
        print('ห้ามใส่ค่าติดลบ') 
r = 0
print('โปรแกรมบวกค่า ถ้าต้องการออกจากโปรแกรมกรุณาพิมพ์ "หยุด"')
while True:
    try:
        num = input('ใส่ค่า : ')
        if num == "หยุด":
            print(f'ผลรวมทั้งหมด {r}')
            print('โปรแกรมสิ้นสุด')
            break

        num = int(num)
        if num == 0:
            raise ZeroDivisionError
                 
        elif num < 0:
            raise Exception

        r = r + num
        print(f'ผลรวมตอนนี้ {r}')
        print('--------------------------------------')

    except ValueError:
        print('ใส่เฉพาะตัวเลข')
    except ZeroDivisionError:
        print('ห้ามใส่ค่าเป็น 0')
    except :
        print('ห้ามใส่ค่าติดลบ')