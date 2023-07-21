# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg kamar = "kamarr"
image bg loby =  "lobby"
image bg smoke = "smokearea"
image bg warnet = "warnett"
image bg kantin = "kantinn"
image bg sampah = "baksampah"

# Deklarasikan karakter yang digunakan di game.
define a = Character('Annisa', color="#000000")
define b = Character('Mama Yudha', color="#000000")
define y = Character(' Yudha', color="#000000")
define k = Character(' Atarik (kating)', color="#000000")
define r = Character(' Krisna', color="#000000")


# Game dimulai disini.
label start:
    play music "audio/SaveTube.io - How We Like It (128 kbps).mp3"

    scene bg kamar with dissolve
    "Pagi yang cerah tiba, burung burung berkicau, suara sepedah anak sekolah terdengar disana sini, dan suara samar bibi menyapu halaman 
    terdengar berisik tapi membuat nyaman"

    "yudha terbangun dari tidurnya yang nyenyak, melihat atap atap langitnya yang kosong, memikirkan 
    masa depan yang akan dihadapi, dibingunkan dengan dua pilihan yang tak pasti"

    "yudha adalah anak yang nakal, anak yang sering 
    berkluyuran malam hari, dan pulang pagi hari, tetapi dia adalah anak yang nurut jika ibunya berkata."

    show mamak marah with dissolve :
        xalign 0.0
        yalign 0.50

    b "YUDHH BANGUN!!!!!"

    hide mamak marah 

    show yudhamarah with dissolve :
        xalign 0.0
        yalign 0.63


    y "UDAH BUUU"

    hide yudhamarah

    show mamak kalem with dissolve :
        xalign 0.0
        yalign 0.50

    b "sini turun sarapan, sama ibu ingin ngomong sesuatu"

    hide mamak kalem

    show yudhasatu with dissolve :
        xalign 0.0
        yalign 0.63

    y "IYA BUUU"

    hide yudhasatu

    "Yudha pun turun dan sarapan bersama keluarganya, piring disitu begitu sunyi, 
    sampai akhirnya ibunya memulai percakapan tentang masa depannya, 
    ibu menyuruh untuk yudha kuliah"

    "sedangkan yudha adalah anak yang ingin sekali bekerja bukan kuliah, 
    terjadi perdebatan dimeja makan itu, sampai akhirnya yudha pun mengalah, dengan syarat memilih kampusnya sendiri."

    "Bulan pun berganti, hari demi hari, detik demi detik, sampai dimana juga yudha akhirnya memasuki masa masa mos perkuliahan."

    scene bg loby with dissolve

    show yudhasedih with dissolve :
        xalign 0.0
        yalign 0.63

    y "HMPH, jadi ini kampusnya, not bad, WUIH ada semoking areanya juga, enak kali ya kesana."

    hide yudhasedih

    stop music fadeout 1.0

    "Tiba tiba ada seseorang  yang menghampiri yudha."

    show katingg with dissolve :
        xalign 0.0
        yalign 0.63
    
    k "woi anak baru, cepat kesana udah ditungguin kaka pembina."

    hide katingg 

    menu:

        "pergi ke smoking area":
            jump choice1_yes

        "pergi ketempat lapangan untuk mengikuti mos":
            jump choice1_no

    label choice1_yes:
        play music "audio/SaveTube.io - Love On File (128 kbps).mp3"

        $ menu_flag = True

        scene bg smoke with dissolve

        "Yudha mengabaikan perintah katingnya untuk menuju ketempat para mahasiswa berkumpul"
        "yudha malah berjalan pada area smoking untuk merokok, yudha bertemu dengan satu orang yang sama dari angkatanya"
        
        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y "woi lu kan sama dari angkatan gua, kenapa lu malah ke SA"

        hide yudhasedih

        show krisnab with dissolve :
            xalign 0.0
            yalign 0.63
        r "Lah lu juga ngapain disini, bukanya ikut kesana"

        hide krisnab

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y "Ya gua asem pen sebat"

        hide yudhasedih

        show krisnab with dissolve :
            xalign 0.0
            yalign 0.63
        r "ya gua sama anjing hahahaha, nama gua kristod, panggil aja krisna lu siapa?"

        hide krisnab

        show yudhasatu with dissolve :
            xalign 0.0
            yalign 0.63
        y "gua romantis yudharasta fara, panggil aja yudha"

        hide yudhasatu

        show krisnab with dissolve :
            xalign 0.0
            yalign 0.63
        "dari pada disini nanti ketauan kating mening kita ke warnet"
        hide krisnab

        scene bg warnet with dissolve

        show yudhamarah with dissolve :
            xalign 0.0
            yalign 0.63
        
        "yudha pun akhirnya ikut ke warnet dengan krisna, setelah itu dia jarang masuk kampus dan tidak menjalai kuliah dengan benar, akhirnya dia pun menjadi op warnnet dengan gaji yang kecil, sialnya dia juga kehilangan motornya."
        return

        jump choice1_done 



    label choice1_no:
        play music "audio/SaveTube.io - Simon's Song (128 kbps).mp3"

        $ menu_flag = False

        "Yudha mengikuti perintah katingnya untuk pergi ketempat mahasiswa berkumpul" 
        "meski rada malas yudha tetap menjalkann tugasnya menjadi mahasiswa, kating berkoar kora sana sini, dengan menyeruakan visi misi kampus."

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y "Halah bullshit (bergumam)"
        hide yudhasedih

        "Tiba tiba seorang yang mendengar gumaman yudha menyaut."

        show nisaa with dissolve :
            xalign 0.0
            yalign 0.63
        a"hahaha sotau kamu, sapa tau yang dibilang itu bener"
        hide nisaa

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y "dih siapa lu nyaut nyaut"
        hide yudhasedih
        
        show nisaa with dissolve :
            xalign 0.0
            yalign 0.63
        a"gua annisa maharani, panggil aja nisa, lu dri prodi mana?"
        hide nisaa

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y "gua yudha dari S1informatika, kalo lu?"
        hide yudhasedih

        show nisaa with dissolve :
            xalign 0.0
            yalign 0.63
        a"gua dari ilmu komunikasi, salam kenal ya yudha"
        hide nisaa

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y "salam kenal juga (apasi ni cewe so asik banget)"
        hide yudhasedih

        "Setelah itu MOS pun berakhir, yudha pulang kerumah dengan lelah setelah melakukan mos di kampus"

        scene bg kamar with dissolve
        
        show mamak kalem with dissolve :
            xalign 0.0
            yalign 0.63
        b "gimana mos nya?"
        hide mamak kalem

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y "lumayan menarik, tadi kenalan dengan beberapa teman juga, udah ya mau istirahat"
        hide yudhasedih

        show mamak kalem with dissolve :
            xalign 0.0
            yalign 0.63
        b "bagus lah kalo begitu yasudah sana istirahat"
        hide mamak kalem

        
        jump choice1_done

    label choice1_done:
 
    scene bg loby with dissolve

    "Besoknya dikampus Yudha kembali mengikuti mos, Yudha secara tidak sengaja bertemu  dengan nisa di kampus saat mau ke kampus."

    show nisaa with dissolve :
            xalign 0.0
            yalign 0.63
    a"eh??? (wajah penuh penasaran) kamu Yudha yang kemarin ya?"
    hide nisaa

    show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
    y"busetdah masih pagi udah ketemu orang ini lagi (bergumam dalam hati)"
    hide yudhasedih

    show yudhasatu with dissolve :
            xalign 0.0
            yalign 0.63
    y"oh, kamu Nisa ya?"
    hide yudhasatu

    show nisaa with dissolve :
            xalign 0.0
            yalign 0.63
    a"mwehehe, kamu kalo ke kampus sendiri kah? Kok ngga bareng temenmu gitu"
    hide nisaa

    show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
    y"ngga"
    hide yudhasedih

    show nisaa with dissolve :
            xalign 0.0
            yalign 0.63
    a"cuek amat ni anak (gumam dalam hati)"

    a"btw kamu waktu istirahat mau kemana yud?"

    hide nisaa

    show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
    y"ga kemana mana sih (muka jutek)"

    hide yudhasedih

    show nisaa with dissolve :
            xalign 0.0
            yalign 0.63
    a"kalo aku sih mau ke kantin ntar, barangkali mau ikut"

    hide nisaa

    show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
    y"ya udah kamu kesana dulu"

    hide yudhasedih

    "Pada akhirnya acara MOS sudah menunjukkan waktu istirahat, si Yudha pun bingung memutuskan untuk kemana waktu jam istirahat"

    y"hmmm mau kemana ya ini enaknya?"

    menu :
        "pergi ke kantin":
            jump choice2_yes
        "pergi ke Smoking Area":    
            jump choice2_no

    label choice2_yes:
        $ menu_flag = True

        scene bg kantin with dissolve
        "Yudha pun memutuskan pergi ke kantin dan membeli makanan atau minuman untuk bersantai disaat waktu istirahat MOS, akan tetapi tiba - tiba Yudha melihat sesosok entitas yang sepertinya dia kenal sebelumnya."
       
        show nisaa with dissolve :
            xalign 0.0
            yalign 0.63
        a"Yud, siniiii duduk disini aja"
        hide nisaa

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y"ohh kamu lagi, ya udah deh aku pesen makanan dulu"
        hide yudhasedih

        show nisaa with dissolve :
            xalign 0.0
            yalign 0.63
        a"sekalian yud aku nitip pesanin es teh jeruk"
        hide nisaa

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y"siappp amann"
        hide yudhasedih

        "Setelah itu si Yudha membawa makanannya dan membawakan juga pesanan Nisa ke tempat si Nisa duduk."
        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y "nih nis pesananmu"
        hide yudhasedih

        show nisab with dissolve :
            xalign 0.0
            yalign 0.63
        a"makasih ya yud, brapa nih totalnya biar aku ganti"
        hide nisab
        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y"ga usah gapapa lah" 
        hide yudhasedih

        show nisab with dissolve :
            xalign 0.0
            yalign 0.63
        a"jangan gitu yud, orang baru kenal kok langsung gini"
        hide nisab

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y"serius kok lagian juga ga sering - sering"
        hide yudhasedih

        show nisab with dissolve :
            xalign 0.0
            yalign 0.63
        a"ya udah deh kalo kamu maksa gitu, makasih ya yud "
        hide nisab

        "pun akhirnya larut dalam perbincangan dengan Nisa di kantin kampus, yang sebelumnya Yudha cuek perlahan jadi sering bicara dengan Nisa."

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y"kamu tuh asal mana sih nis, kok aku belum tau"

        show nisab with dissolve :
            xalign 0.0
            yalign 0.63
        a"aku asal kalimantan yud, kalau kamu?"
        hide nisab

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y"wehhh sama dong aku juga asal situ"

        y"aku kesini sendiri njirrr belum ada temen yang dari asalku, jadi aku belum banyak kenalan disini"
        hide yudhasedih

        show nisab with dissolve :
            xalign 0.0
            yalign 0.63
        a" ummmm kesempatan yang bagus nih buat ngedeketin si Yudha (gumam dalam hati)"

        a"aku juga gitu yud, makanya akhir - akhir ini aku sering ngajak ngobrol kamu (ekspresi malu - malu)"
        hide nisab

        show yudhasatu with dissolve :
            xalign 0.0
            yalign 0.63
        y"ehhh (terkejut)"
        hide yudhasatu

        show nisab with dissolve :
            xalign 0.0
            yalign 0.63
        a"santai aja kali lagian kita disini juga biar saling kenal ya kan"
        hide nisab

    jump choice2_done

    label choice2_no:
        $ menu_flag = False

        scene bg smoke

        "Yudha pun memutuskan pergi ke smoking area untuk bersantai sambil menyalakan rokok disaat waktu istirahat MOS, tak lama kemudian datanglah Krisna ke smoking area juga."
        show krisnaa with dissolve :
            xalign 0.0
            yalign 0.63
        r"hmmm bro kyanya lu satu angkatan sama gua kan "
        hide krisnaa

        show yudhasatu with dissolve :
            xalign 0.0
            yalign 0.63
        y"iya bang gua satu prodi, nama gua yudha salam kenal."
        hide yudhasatu

        show krisnaa with dissolve :
            xalign 0.0
            yalign 0.63
        r"gua krisna bang salam kenal, bang lu abis ini mau kemana bang?"
        hide krisnaa

        show yudhasatu with dissolve :
            xalign 0.0
            yalign 0.63
        y"lanjut lagi mungkin ikut mos"
        hide yudhasatu

        show krisnaa with dissolve :
            xalign 0.0
            yalign 0.63
        r"mening bolos aja bang, gua abis ini mau ke club, minum minum, ikut ga?"
        hide krisnaa

        show yudhasatu with dissolve :
            xalign 0.0
            yalign 0.63
        y"boleh dah ikut gua "
        hide yudhasatu

        scene bg sampah with dissolve

        show yudhamarah with dissolve :
            xalign 0.0
            yalign 0.63

        "Yudha pun akhirnya mengikuti krisna ke club, setelah itu dia kecanduan ke club untuk mabuk mabukan, hidupnya menjadi kacau dan menjadi gelandangan."

        return

        jump choice2_done

    label choice2_done:

        scene bg kamar

        show yudhasedih with dissolve :
            xalign 0.0
            yalign 0.63
        y"ko makin hari gua makin deket ya sama nisa, atau gua nya aja yang ngerasa gitu, trus entah kenapa kalo gua dekat dengan dia, gua ngerasa nyaman didekatnya, hmm ane rasanya."

        hide yudhasedih

        "Yudha yang merasa bimbang dengan perasaanya mulai mencari jawaban akan hatinya, apakah dia merasasa suka kepada nisa sebagai lawan jenis"
        "atau merasa nissa adalah teman yang nyaman untuk diajak bicara dan untuk menemani kemana mana
        cerita ini akan di lanjut ke dalam chapter 2 terimakasih.."
    return