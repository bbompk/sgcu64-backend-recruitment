import time

locations = ['Mahamakut Building', 
    'Sara phra keaw',
    'CU sport complex',
    'Sanam Juub',
    'Samyan Mitrtown',
] 
data = [
    ['8036046920','7805984816','7633009694','3757987595','4341833235','3237319479','4619748910' ] ,
    ['3786638737','6827525926','8597709830','9058787792','4352338959','4936846560','4692023429','1705797605','1049445005'],
    ['6741585867','7095951884','9216731765','7686744417','5115585585','9539267311','2746791345','4221924178','7535072112','7167966626','3318244602'],
    ['2412626149','7916474786','2174530661','5584364196','4763551107','6205950444','6343190841'],
    ['9276393871','9495657567','2909414823','8366008889','2865115669','3852676801','5729736808','1448778479','1167006669','1058599069','4431138301','8868973786','6592571796','6167019600','2703724582','5849815446','3378303351','1921437092','4179802372']
]

def Op() :
    print('Welcome to Chula Chana!\nCommands:')
    print('     1.Check in\n     2.Check out\n     3.See Population\n     4.Quit')
    c = input('Enter command (No.): ') 
    print()
    if c == '1' :
        print('Check In')
        phone_no = input('Enter phone number : ')
        for i in range(len(locations)) :
            print('     '+str(i+1)+'.'+locations[i])
        print('     '+str(len(locations)+1)+'.Other Location')
        location_ind = int(input('Enter location (No.) : '))-1
        if location_ind == len(locations) :
            new_lo = input('Enter the new location name: ')
            locations.append(new_lo)
            data.append([])  
        if phone_no not in data[location_ind] :
            for i in range(len(data)) :
                if phone_no in data[i] :
                    data[i].remove(phone_no)
                    print('     Checked out from '+locations[i])
            data[location_ind].append(phone_no)
            print('     Checked in to '+locations[location_ind])
    if c == '2' :
        print('Check out')
        phone_no = input('Enter phone number : ')
        is_in = False
        for i in range(len(data)) :
                if phone_no in data[i] :
                    print(data[i])
                    data[i].remove(phone_no)
                    print('     Checked out from '+locations[i])
                    is_in = True
        if not is_in :
            print('     You haven\'t checked in')
    if c == '3' :
        print('Current Population')
        for i in range(len(locations)) :
            print('     '+str(i+1)+'.'+locations[i]+' : '+str(len(data[i])))
        input('Enter anything to continue:')
    if c == '4' :
        return 0
    return 1

def main() :
    while Op() :
        cd = 3
        while cd :
            print('     returning to main menu '+str(cd),end='\r')
            cd-=1
            time.sleep(1)
        print('     returning to main menu 0')
        print('\n-----------------------------\n')


main()
