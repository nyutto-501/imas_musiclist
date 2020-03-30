import glob

path = '/Users/user/Music/MUSIC/'
offices = ['765PRO ALLSTARS/', 'CINDERELLA/', 'MILLION LIVE/', 'SHINY COLORS/', 'SideM/']

for office in offices:
    music = glob.glob(path + office + '*.mp3')
    m4a = glob.glob(path + office + '*.m4a')
    music.extend(m4a)
    for i in range(len(music)):
        music[i] = 'C:' + music[i].replace('/', '\\')

    with open('playlist.txt', 'a', encoding='utf-8') as f:
        for hoge in music:
            f.write(hoge + '\n')
