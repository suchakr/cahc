// SSC include file that N27 and N89 info and some utility functions and constants
var $NAKSHATRAS =
  [
    {
      "nid": "N01",
      "tara": "अश्विनी",
      "rasi": "मेषः",
      "star": "Hamal",
      "hip": "HIP 9884",
      "naks": "Ashwini"
    },
    {
      "nid": "N02",
      "tara": "भरणी",
      "rasi": "मेषः",
      "star": "Bharani",
      "hip": "HIP 13209",
      "naks": "Bharani"
    },
    {
      "nid": "N03",
      "tara": "कृत्तिका",
      "rasi": "वृषभः",
      "star": "Alcyone",
      "hip": "HIP 17702",
      "naks": "Krittika"
    },
    {
      "nid": "N04",
      "tara": "रोहिणी",
      "rasi": "वृषभः",
      "star": "Aldebaran",
      "hip": "HIP 21421",
      "naks": "Rohini"
    },
    {
      "nid": "N05",
      "tara": "मृगशीर्षा",
      "rasi": "मिथुनः",
      "star": "Meissa",
      "hip": "HIP 26207",
      "naks": "Mrigashirisham"
    },
    {
      "nid": "N06",
      "tara": "आर्द्रा",
      "rasi": "मिथुनः",
      "star": "Betelgeuse",
      "hip": "HIP 27989",
      "naks": "Thiruvadarai"
    },
    {
      "nid": "N07",
      "tara": "पुनर्वसू (द्वि)",
      "rasi": "मिथुनः",
      "star": "Pollux",
      "hip": "HIP 37826",
      "naks": "Punarpasu"
    },
    {
      "nid": "N08",
      "tara": "पुष्या;तिष्या",
      "rasi": "कर्कः",
      "star": "Asellus Australis",
      "hip": "HIP 42911",
      "naks": "Pushyam"
    },
    {
      "nid": "N09",
      "tara": "आश्लेषा",
      "rasi": "कर्कः",
      "star": "Minazal V",
      "hip": "HIP 43813",
      "naks": "Ayilyam"
    },
    {
      "nid": "N10",
      "tara": "मघा",
      "rasi": "सिंहः",
      "star": "Regulus",
      "hip": "HIP 49669",
      "naks": "Makam"
    },
    {
      "nid": "N11",
      "tara": "पूर्वफल्गुनी",
      "rasi": "सिंहः",
      "star": "Zozma",
      "hip": "HIP 54872",
      "naks": "Pooram"
    },
    {
      "nid": "N12",
      "tara": "उत्तरफल्गुनी",
      "rasi": "कन्या",
      "star": "Cheratan",
      "hip": "HIP 54879",
      "naks": "Uttiram"
    },
    {
      "nid": "N13",
      "tara": "हस्ता",
      "rasi": "कन्या",
      "star": "Algorab",
      "hip": "HIP 60965",
      "naks": "Hastam"
    },
    {
      "nid": "N14",
      "tara": "चित्रा",
      "rasi": "कन्या",
      "star": "Spica",
      "hip": "HIP 65474",
      "naks": "Chitrai"
    },
    {
      "nid": "N15",
      "tara": "स्वाती",
      "rasi": "तुला",
      "star": "Arcturus",
      "hip": "HIP 69673",
      "naks": "Swati"
    },
    {
      "nid": "N16",
      "tara": "विशाखा",
      "rasi": "तुला",
      "star": "Zubenelgenubi",
      "hip": "HIP 72603",
      "naks": "Vishakam"
    },
    {
      "nid": "N17",
      "tara": "अनुराधा",
      "rasi": "वृश्चिका",
      "star": "Dschubba",
      "hip": "HIP 78401",
      "naks": "Anusham"
    },
    {
      "nid": "N18",
      "tara": "ज्येष्ठा",
      "rasi": "वृश्चिका",
      "star": "Antares",
      "hip": "HIP 80763",
      "naks": "Kettai"
    },
    {
      "nid": "N19",
      "tara": "मूला",
      "rasi": "धनुः",
      "star": "Shaula",
      "hip": "HIP 85927",
      "naks": "Moolam"
    },
    {
      "nid": "N20",
      "tara": "पूर्व्वाषाढा",
      "rasi": "धनुः",
      "star": "Kaus Australis",
      "hip": "HIP 90185",
      "naks": "Pooradam"
    },
    {
      "nid": "N21",
      "tara": "उत्तराषाढा",
      "rasi": "धनुः",
      "star": "Nunki",
      "hip": "HIP 92855",
      "naks": "Uttiradam"
    },
    {
      "nid": "N22",
      "tara": "श्रवणा",
      "rasi": "मकरः",
      "star": "Altair",
      "hip": "HIP 97649",
      "naks": "Thiruvonam"
    },
    {
      "nid": "N23",
      "tara": "धनिष्ठा",
      "rasi": "मकरः",
      "star": "Sualocin",
      "hip": "HIP 101958",
      "naks": "Avittam"
    },
    {
      "nid": "N24",
      "tara": "शतभिषक्",
      "rasi": "कुम्भः",
      "star": "Situla",
      "hip": "HIP 111710",
      "naks": "Shatayam"
    },
    {
      "nid": "N25",
      "tara": "पूर्वभाद्रपदा",
      "rasi": "कुम्भः",
      "star": "Markab",
      "hip": "HIP 113963",
      "naks": "Poorattadi"
    },
    {
      "nid": "N26",
      "tara": "उत्तरभाद्रपदा",
      "rasi": "मीना",
      "star": "Alpheratz",
      "hip": "HIP 677",
      "naks": "Uttiratadi"
    },
    {
      "nid": "N27",
      "tara": "रेवती",
      "rasi": "मीना",
      "star": "Alrischa",
      "hip": "HIP 9487",
      "naks": "Revati"
    },
    {
      "nid": "N28",
      "tara": "अभिजित्",
      "rasi": "मकरः",
      "star": "Vega",
      "hip": "HIP 91262",
      "naks": "Abhijit"
    }
  ];
var $N27 = $NAKSHATRAS

var $GRUHAS = ['Jupiter', 'Mars', 'Mercury', 'Moon', 'Saturn', 'Sun', 'Venus']

var $JD_0_JAN_1 = 1721057.284468
var $JD_BCE_3000_JAN_1 = 625332.5  // -3000 - 01 - 01T00: 00: 00.000
var $JD_KALI_YUGA_JEPPY = 588465.5  // -3101 - 01 - 23T00: 00: 00.000(+25 gets to KY 17 / Feb / -3101)
var $JD_JEPPY_OFFSET = 2415020   // 1899 - 12 - 31T12: 00: 00.00

var $JD_KALI = $JD_KALI_YUGA_JEPPY
var $JD_0 = $JD_0_JAN_1

function BCE(y)  { return  $JD_0 - (y-1)*365.25 }
function CE(y)  { return  $JD_0 + y*365.25 }

function say(x) { core.debug('' + x) }
function warn(x) { core.output('' + x) }
function W(x) { if (!x) x = 0.1; core.wait(x) }
function JD(x) { if (x) { core.setJDay(x); W() } return core.getJDay() }
function DT(x, tzin, tzout) { if (x) { core.setDate(x,tzin?tzin:"utc" ); W() } return core.getDate(tzout?tzout:"local") }
var $WRITE_X = 100
var $WRITE_Y = 80
function hexof(d) { return '01234567890ABCDEF'[d%16] }
function cls() { LabelMgr.deleteAllLabels(); $WRITE_Y=80}
function writes(t,color, size,wait) { // write to screen
  if (!size) size=10
  if (!color) color= '#CCC' + hexof($WRITE_Y) + hexof($WRITE_Y) + hexof($WRITE_Y) //+ hexof($WRITE_X) + 'FF' 
  var id = LabelMgr.labelScreen(t, $WRITE_X, $WRITE_Y, false, size , color);
  LabelMgr.setLabelShow(id, true);
  $WRITE_Y += (size+2) 
  if (!wait)
  core.wait(wait)
}
var $TITLE_X = 400
var $TITLE_Y = 200 
function titles(t,color, size, wait) { // title to screen
  if (!size) size=25
  var x=$TITLE_X
  var y=$TITLE_Y
  if (!color) color= '#ABC' + hexof(y) + hexof(y) + hexof(y) //+ hexof($WRITE_X) + 'FF' 
  var id = LabelMgr.labelScreen(t, x, y, false, size , color);
  LabelMgr.setLabelShow(id, true);
  $TITLE_Y += (size+2) 
  if(!wait) wait=.5
  core.wait(wait)
  return id
}

function writeat(x, y, txt, color, size, wait) {
  savex = $WRITE_X;
  savey = $WRITE_Y;
  $WRITE_X = x;
  $WRITE_Y = y;
  writes(txt, color, size);
  if ( !wait ) wait = .1;  W(wait);
  $WRITE_X = savex;
  $WRITE_Y = savey;

}

var id = LabelMgr.labelScreen("Tour of 27 Nakshatras", 500, 500, false, 30)

function TimeKeeper() {
   this.start = (new Date()).getTime()
   this.secElapsed = function() {
    var ms = ((new Date()).getTime() - this.start)
    return Math.round(ms / 1000)
  }
}

getOI = core.getObjectInfo

function ddump(x, pretty) {
  if (pretty) {
    JSON.stringify(x, '', "\n").split("\n").forEach(function (x) { say(x) })
  } else {
    say(JSON.stringify(x, '', "\n"))
  }
}

function GetNaksLatLongWithDegreesPerCentury($start_jd, $years_per_step, $num_steps) {
  if ($start_jd === undefined) $start_jd = 1501914.5  // 600-1-1 BCE
  if ($years_per_step === undefined) $years_per_step = 100  // take reading every century
  if ($num_steps === undefined) $num_steps = 4  // take reading for 4 centuries 
  say(['nid', 'nname', 'date', 'jd', 'long', 'lat', 'long_rate_dpc', 'lat_rate_dpc'].join("\t")) // dps = degrees per century
  $NAKSHATRAS.forEach(function (e) {
    var os = []
    for (var i = 0; i < 4; i++) {
      var jd = JD($start_jd + i * $years_per_step * 365.25); W(.05)
      var o = core.getObjectInfo(e.hip); W(.5)
      o.jd = jd
      os.push(o)
    }
    var long_diff_sum = 0
    var lat_diff_sum = 0
    var jd_diff_sum = 0
    for (var i = 1; i < os.length; i++) {
      long_diff_sum += (os[i].elong - os[i - 1].elong)
      lat_diff_sum += (os[i].elat - os[i - 1].elat)
      jd_diff_sum += (os[i].jd - os[i - 1].jd)
    }
    var long_diff_avg = 100 * 365.25 * long_diff_sum / (jd_diff_sum)
    var lat_diff_avg = 100 * 365.25 * lat_diff_sum / (jd_diff_sum)
    // var long_diff_avg = long_diff_sum / (os.length - 1)
    // var lat_diff_avg = lat_diff_sum / (os.length - 1)
    long_diff_avg = Math.round(long_diff_avg * 1000) / 1000
    lat_diff_avg = Math.round(lat_diff_avg * 1000) / 1000
    var mido = os[os.length / 2]
    JD(mido.jd)
    say([e.nid, e.naks, DT(), JD(), Math.round(mido.elong * 1000) / 1000, Math.round(mido.elat * 1000) / 1000, long_diff_avg, lat_diff_avg].join("\t"))
  })
}
var GetN27LatLong = GetNaksLatLongWithDegreesPerCentury

function GetGruhasLatLong($start_jd, $days_per_step, $num_steps) {
  if ($start_jd === undefined) $start_jd = 1501914.5  // 600-1-1 BCE
  if ($days_per_step === undefined) $days_per_step = 100  // take reading every century
  if ($num_steps === undefined) $num_steps = 4  // take reading for 4 centuries 
  say(['pname', 'date', 'jd', 'long', 'lat', 'long_rate_dpd', 'lat_rate_dpd'].join("\t")) // dps = degrees per century
  $GRUHAS.forEach(function (e) {
    var os = []
    for (var i = 0; i < 4; i++) {
      var jd = JD($start_jd + i * $days_per_step); W(.05)
      var o = core.getObjectInfo(e); W(.5)
      o.jd = jd
      os.push(o)
    }
    var long_diff_sum = 0
    var lat_diff_sum = 0
    var jd_diff_sum = 0
    for (var i = 1; i < os.length; i++) {
      long_diff_sum += (os[i].elong - os[i - 1].elong)
      lat_diff_sum += (os[i].elat - os[i - 1].elat)
      jd_diff_sum += (os[i].jd - os[i - 1].jd)
    }
    var long_diff_avg = long_diff_sum / (jd_diff_sum)
    var lat_diff_avg = lat_diff_sum / (jd_diff_sum)
    // var long_diff_avg = long_diff_sum / (os.length - 1)
    // var lat_diff_avg = lat_diff_sum / (os.length - 1)
    long_diff_avg = Math.round(long_diff_avg * 1000) / 1000
    lat_diff_avg = Math.round(lat_diff_avg * 1000) / 1000
    var mido = os[os.length / 2]
    JD(mido.jd)
    say([e, DT(), JD(), Math.round(mido.elong * 1000) / 1000, Math.round(mido.elat * 1000) / 1000, long_diff_avg, lat_diff_avg].join("\t"))
  })
}

var header_n89 = "#	nid	naks	main_id	name	HIP	mag	bri	ra	dec	Long	Lat".toLowerCase().split(/\t/)
var $N89 = [
  "1	N03-Kri	क्रित्तिकाः	* eta Tau	Alcyone	HIP  17702	2.9	4	56.87	24.11	11.4931	3.7089",
  "2	N03-Kri	क्रित्तिकाः	* 17 Tau	Electra	HIP  17499	3.7	3	56.22	24.11	10.9129	3.8531",
  "3	N03-Kri	क्रित्तिकाः	* q Tau	Taygeta	HIP  17531	4.3	3	56.3	24.47	11.0674	4.1791",
  "4	N03-Kri	क्रित्तिकाः	* 20 Tau	Maia	HIP  17573	3.9	3	56.46	24.37	11.1809	4.0501",
  "5	N03-Kri	क्रित्तिकाः	* 23 Tau	Merope	HIP  17608	4.2	3	56.58	23.95	11.201	3.6177",
  "6	N03-Kri	क्रित्तिकाः	* 27 Tau	Atlas	HIP  17847	3.6	3	57.29	24.05	11.8567	3.5748",
  "7	N03-Kri	क्रित्तिकाः	* 28 Tau	Pleione	HIP  17851	5.1	2	57.3	24.14	11.8799	3.6577",
  "8	N04-Roh	रोहिणी	* alf Tau	Aldebaran	HIP  21421	0.9	6	68.98	16.51	21.2258	-5.6968",
  "9	N04-Roh	रोहिणी	* gam Tau	Prima Hyadum	HIP  20205	3.7	3	64.95	15.63	17.1632	-6.1039",
  "10	N04-Roh	रोहिणी	* del Tau	Secunda Hyadum	HIP  20455	3.8	3	65.73	17.54	18.2445	-4.3411",
  "11	N04-Roh	रोहिणी	* eps Tau	Ain	HIP  20889	3.5	3	67.15	19.18	19.8466	-2.9379",
  "12	N04-Roh	रोहिणी	* tet02 Tau	Chamukuy	HIP  20894	3.4	4	67.17	15.87	19.3283	-6.2166",
  "13	N05-Mrg	मृगशीर्षः	* gam Ori	Bellatrix	HIP  25336	1.6	5	81.28	6.35		",
  "14	N05-Mrg	मृगशीर्षः	* phi01 Ori	lambda Ori X-5	HIP  26176	4.4	3	83.71	9.49		",
  "15	N05-Mrg	मृगशीर्षः	* lam Ori	Heka	HIP  26207	3.7	3	83.78	9.93		",
  "16	N06-Ard	आर्द्रा	* alf Ori	Betelgeuse	HIP  27989	0.4	7	88.79	7.41		",
  "17	N07-Pun	पुनर्वसू	* bet Gem	Pollux	HIP  37826	1.1	6	116.33	28.03		",
  "18	N07-Pun	पुनर्वसू	* alf Gem	Castor	HIP  36850	1.6	5	113.65	31.89		",
  "19	N08-Pus	पुष्यः	* del Cnc	Asellus Australis	HIP  42911	3.9	3	131.17	18.15		",
  "20	N09-Asl	आश्लेषः	* del Hya	xxx	HIP  42313	4.1	3	129.41	5.7		",
  "21	N09-Asl	आश्लेषः	* sig Hya	Minchir	HIP  42402	4.4	3	129.69	3.34		",
  "22	N09-Asl	आश्लेषः	* eta Hya	xxx	HIP  42799	4.3	3	130.81	3.4		",
  "23	N09-Asl	आश्लेषः	* eps Hya	Ashlesha	HIP  43109	3.4	4	131.69	6.42		",
  "24	N09-Asl	आश्लेषः	* rho Hya	xxx	HIP  43234	4.3	3	132.11	5.84		",
  "25	N09-Asl	आश्लेषः	* zet Hya	xxx	HIP  43813	3.1	4	133.85	5.95		",
  "26	N10-Mag	मघाः	* alf Leo	Regulus	HIP  49669	1.4	6	152.09	11.97	152.093	11.96721",
  "27	N10-Mag	मघाः	* eps Leo	xxx	HIP  47908	3	4	146.46	23.77		",
  "28	N10-Mag	मघाः	* mu. Leo	Rasalas	HIP  48455	3.9	3	148.19	26.01	148.1909	26.00695",
  "29	N10-Mag	मघाः	* eta Leo	xxx	HIP  49583	3.4	4	151.83	16.76		",
  "30	N10-Mag	मघाः	* zet Leo	Adhafera	HIP  50335	3.4	4	154.17	23.42	154.1726	23.41731",
  "31	N10-Mag	मघाः	* gam Leo	Algieba	HIP  50583	2.4	5	154.99	19.84	154.9931	19.84149",
  "32	N11-PPal	पूर्वफल्गुनी	* del Leo	Zosma	HIP  54872	2.5	4	168.53	20.52		",
  "33	N11-PPal	पूर्वफल्गुनी	* tet Leo	Chertan	HIP  54879	3.4	4	168.56	15.43		",
  "34	N12-UPal	उत्तरफल्गुनी	* bet Leo	Denebola	HIP  57632	2.1	5	177.26	14.57		",
  "35	N12-UPal	उत्तरफल्गुनी	* 93 Leo	xxx	HIP  57565	4.5	2	177	20.22		",
  "36	N13-Has	हस्तः	* del Crv	Algorab	HIP  60965	2.9	4	187.47	-16.52		",
  "37	N13-Has	हस्तः	* alf Crv	Alchiba	HIP  59199	4	3	182.1	-24.73		",
  "38	N13-Has	हस्तः	* eps Crv	Minkar	HIP  59316	3	4	182.53	-22.62		",
  "39	N13-Has	हस्तः	* gam Crv	Gienah	HIP  59803	2.6	4	183.95	-17.54		",
  "40	N13-Has	हस्तः	* bet Crv	Kraz	HIP  61359	2.6	4	188.6	-23.4		",
  "41	N14-Chi	चित्रा	* alf Vir	Spica	HIP  65474	1	6	201.3	-11.16		",
  "42	N15-Swa	स्वाती	* alf Boo	Arcturus	HIP  69673	-0.1	7	213.92	19.18		",
  "43	N16-Vis	विशाखे	* alf02 Lib	Zubenelgenubi	HIP 72622	2.8	4	222.72	-16.04		",
  "44	N17-Anu	अनूराधा	* del Sco	Dschubba	HIP  78401	2.3	5	240.08	-22.62		",
  "45	N17-Anu	अनूराधा	* pi. Sco	Fang	HIP  78265	2.9	4	239.71	-26.11		",
  "46	N17-Anu	अनूराधा	* bet02 Sco	Acrab	HIP 78221	2.5	4	241.36	-19.81		",
  "47	N17-Anu	अनूराधा	* ome Sco	xxx	HIP  78933	4	3	241.7	-20.67		",
  "48	N18-Jye	ज्येष्ठा	* alf Sco	Antares	HIP  80763	0.9	6	247.35	-26.43	250.06	-4.57",
  "49	N18-Jye	ज्येष्ठा	* sig Sco	Alniyat	HIP 80112A	3.05		245.62	-25.64	248.1	-4.04",
  "50	N18-Jye	ज्येष्ठा	* tau Sco	Alniyat II	HIP 81266	2.8		248.98	-28.22	251.75	-6.12",
  "51	N19-Mul	मूलं	* lam Sco	Shaula	HIP  85927	1.6	5	263.4	-37.1	264.88	-13.79",
  "52	N19-Mul	मूलं	* tet Sco	Sargas	HIP  86228	1.9	5	264.33	-43	265.9	-19.65",
  "53	N19-Mul	मूलं	* nu Sco	Lesath	HIP 85696	2.7		263.06	-37.31	264.31	-14.01",
  "54	N19-Mul	मूलं	* Zet2 Sco		HIP 82729	3.6		262.02	-42.4	257.54	-19.65",
  "55	N19-Mul	मूलं	* iot Sco	Girtab	HIP 87073	2.95		267.27	-40.13	267.82	-16.72",
  "56	N19-Mul	मूलं	* kap Sco	Mula	HIP 86670	2.35		265.99	-39.04	266.77	-16.65",
  "57	N20-PAsh	पूर्वाषाढा	* eps Sgr	Kaus Australis	HIP  90185	1.9	5	276.04	-34.38		",
  "58	N20-PAsh	पूर्वाषाढा	* gam02 Sgr	Alnasl	HIP  88635	3	4	271.45	-30.42		",
  "59	N20-PAsh	पूर्वाषाढा	* del Sgr	Kaus Media	HIP  89931	2.7	4	275.25	-29.83		",
  "60	N20-PAsh	पूर्वाषाढा	* lam Sgr	Kaus Borealis	HIP  90496	2.8	4	276.99	-25.42		",
  "61	N21-UAsh	उत्तराषाढा	* sig Sgr	Nunki	HIP  92855	2.1	5	283.82	-26.3		",
  "62	N21-UAsh	उत्तराषाढा	* phi Sgr	xxx	HIP  92041	3.1	4	281.41	-26.99		",
  "63	N21-UAsh	उत्तराषाढा	* zet Sgr	Ascella	HIP  93506	2.6	4	285.65	-29.88		",
  "64	N21-UAsh	उत्तराषाढा	* tau Sgr	xxx	HIP  93864	3.3	4	286.74	-27.67		",
  "65	N28-Abh	अभिजित्	* alf Lyr	Vega	HIP  91262	0	7	279.23	38.78		",
  "66	N28-Abh	अभिजित्	* eps01 Lyr	xxx	HIP  91919	4.7	2	281.08	39.67		",
  "67	N28-Abh	अभिजित्	* zet01 Lyr	xxx	HIP  91971	4.4	3	281.19	37.61		",
  "68	N22-Shr	श्रवणः	* alf Aql	Altair	HIP  97649	0.8	6	297.7	8.87		",
  "69	N22-Shr	श्रवणः	* gam Aql	Tarazed	HIP  97278	2.7	4	296.56	10.61		",
  "70	N22-Shr	श्रवणः	* bet Aql	Alshain	HIP  98036	3.7	3	298.83	6.41		",
  "71	N23-Dha	धनिष्ठा	* alf Del	Sualocin	HIP 101958	3.8	3	309.91	15.91		",
  "72	N23-Dha	धनिष्ठा	* eps Del	Aldulfin	HIP 101421	4	3	308.3	11.3		",
  "73	N23-Dha	धनिष्ठा	* bet Del	Rotanev	HIP 101769	3.6	3	309.39	14.6		",
  "74	N23-Dha	धनिष्ठा	* del Del	xxx	HIP 102281	4.4	3	310.86	15.07		",
  "75	N23-Dha	धनिष्ठा	* gam02 Del	xxx	HIP 102532 A	3.9	3	311.66	16.12		",
  "78	N24-Sha	शतभिषक्	* lam Aqr	xxx	HIP 112961	3.8	3	343.15	-7.45	341.88	-0.39",
  "79	N25-PBha	पूर्वाभाद्रपदा	* alf Peg	Markab	HIP 113963	2.5	5	346.19	15.21		",
  "80	N25-PBha	पूर्वाभाद्रपदा	* bet Peg	Scheat	HIP 113881	2.4	5	345.94	28.08		",
  "81	N26-UBha	उत्तराभाद्रपदा	* alf And	Alpheratz	HIP    677	2.1	5	2.1	29.09		",
  "82	N26-UBha	उत्तराभाद्रपदा	* gam Peg	Algenib	HIP   1067	2.8	4	3.31	15.18		",
  "83	N27-Rev	रेवती	* alf Psc	Alrescha	HIP   9487	3.8	3	30.51	2.76	29.68	-9.06",
  "84	N01-Ash	अश्विनी	* alf Ari	Hamal	HIP   9884	2	5	31.79	23.46	37.96	9.97",
  "85	N01-Ash	अश्विनी	* bet Ari	Sheratan	HIP   8903	2.7	4	28.66	20.81	34.27	8.49",
  "86	N01-Ash	अश्विनी	* gam Ari	Mesarthim	HIP 8832A	4.5		28.68	19.4	33.48	7.16",
  "87	N02-Bha	भरणी	* 41 Ari	Bharani	HIP  13209	3.6	3	42.5	27.26	48.5	10.45",
  "88	N02-Bha	भरणी	* 31 Ari	xxx	HIP  12153	5.7	1	39.16	12.45		",
  "89	N02-Bha	भरणी	* 35 Ari	xxx	HIP  12719	4.7	2	40.86	27.71"]
  .map(function (v) { return v.split("\t") })
  .map(function (v) {
    var h = {}
    v.map(function (e, i) {
      h[header_n89[i]] = e //.replace(/HIP\s+/,'')
    })
    return h
  }).map(function (v) {
    v.hip = v.hip.replace(/\s*\D+\s*$/, '')
    return v
  })

function GetN89LatLong($start_jd, $years_per_step, $num_steps) {
  if ($start_jd === undefined) $start_jd = 1501914.5  // 600-1-1 BCE
  if ($years_per_step === undefined) $years_per_step = 100  // take reading every century
  if ($num_steps === undefined) $num_steps = 3  // take reading for 4 centuries 
  say(['#', 'nid', 'naks', 'name', 'tname', 'hip', 'jd', 'long', 'lat', 'ra', 'dec', 'long_rate_dpc', 'lat_rate_dpc', 'date'].join("\t")) // dps = degrees per century
  $N89.forEach(function (e, idx) { //if ( idx > 2) return;
    var os = []
    for (var i = 0; i < 4; i++) {
      var jd = JD($start_jd + i * $years_per_step * 365.25); W(.05)
      var o = core.getObjectInfo(e.hip); W(.5)
      o.jd = jd
      os.push(o)
    }
    var long_diff_sum = 0
    var lat_diff_sum = 0
    var jd_diff_sum = 0
    for (var i = 1; i < os.length; i++) {
      long_diff_sum += (os[i].elong - os[i - 1].elong)
      lat_diff_sum += (os[i].elat - os[i - 1].elat)
      jd_diff_sum += (os[i].jd - os[i - 1].jd)
    }
    var long_diff_avg = 100 * 365.25 * long_diff_sum / (jd_diff_sum)
    var lat_diff_avg = 100 * 365.25 * lat_diff_sum / (jd_diff_sum)
    // var long_diff_avg = long_diff_sum / (os.length - 1)
    // var lat_diff_avg = lat_diff_sum / (os.length - 1)
    long_diff_avg = Math.round(long_diff_avg * 1000) / 1000
    lat_diff_avg = Math.round(lat_diff_avg * 1000) / 1000
    var mido = os[os.length / 2]
    JD(mido.jd)
    // ddump(mido, "pretty")
    say([e['#'], e.nid, e.naks, e.name, e.main_id, e.hip, JD(),
    Math.round(mido.elong * 1000) / 1000, Math.round(mido.elat * 1000) / 1000,
    Math.round(mido.ra * 1000) / 1000, Math.round(mido.dec * 1000) / 1000,
      long_diff_avg, lat_diff_avg, DT()].join("\t"))
  })
}

var header_naks = "nid	naks	gname	name	HIP".toLowerCase().split(/\t/)
var $N27Feb20 = [
  "N01-Ash	अश्विनी	β Ari	Sheratan	HIP 8903",
  "N02-Bha	भरणी	* 41 Ari	Bharani	HIP 13209",
  "N03-Kri	क्रित्तिकाः	η Tau	Alcyone	HIP 17702",
  "N04-Roh	रोहिणी	α Tau	Aldebaran	HIP  21421",
  "N05-Mrg	मृगशीर्षः	λ Ori	Meissa(Heka)	HIP  26207",
  "N06-Ard	आर्द्रा	α Ori	Betelgeuse	HIP  27989",
  //"N06-Ard	आर्द्रा	γ Gem	Alhena(Almeisan)	HIP 31681",
  "N07-Pun	पुनर्वसू	β Gem	Pollux	HIP  37826",
  "N08-Pus	पुष्यः	δ Cnc	Asellus Australis	HIP  42911",
  "N09-Asl	आश्लेषः	ζ Hya	Minazal V	HIP 43813",
  "N10-Mag	मघाः	α Leo	Regulus	HIP  49669",
  // "N10-Mag	मघाः	ζ Leo	Adhafera	HIP 50335",
  "N11-PPal	पूर्वफल्गुनी	δ Leo	Zosma	HIP  54872",
  "N12-UPal	उत्तरफल्गुनी	β Leo	Denebola	HIP  57632",
  "N13-Has	हस्तः	δ Crv	Algorab	HIP  60965",
  "N14-Chi	चित्रा	α Vir	Spica	HIP  65474",
  "N15-Swa	स्वाती	α Boo	Arcturus	HIP  69673",
  "N16-Vis	विशाखे	α2 Lib	Zubenelgenubi	HIP 72622",
  "N17-Anu	अनूराधा	δ Sco	Dschubba	HIP  78401",
  "N18-Jye	ज्येष्ठा	α Sco	Antares	HIP  80763",
  // "N18-Jye	ज्येष्ठा	ε Sco	Larawag	HIP  82396",
  "N19-Mul	मूलं	λ Sco	Shaula	HIP  85927",
  // "N19-Mul	मूलं	κ Sco	Mula	HIP  86670",
  "N20-PAsh	पूर्वाषाढा	λ Sgr	Kaus Borealis	HIP  90496",
  // "N20-PAsh	पूर्वाषाढा	φ Sgr	Namalsadirah I	HIP 92041",
  "N21-UAsh	उत्तराषाढा	τ Sgr	xxx	HIP  93864",
  // "N21-UAsh	उत्तराषाढा	η Sgr	Hamalwarib(Arkab)	HIP  89462",
  "N22-Shr	श्रवणः	α Aql	Altair	HIP  97649",
  "N23-Dha	धनिष्ठा	β Del	Rotanev	HIP 101769",
  "N24-Sha	शतभिषक्	λ Aqr	Hydor	HIP 112961",
  "N25-PBha	पूर्वाभाद्रपदा	α Peg	Markab	HIP 113963",
  // "N26-UBha	उत्तराभाद्रपदा	λ Peg	Sadalnazi	HIP 112440",
  "N26-UBha	उत्तराभाद्रपदा	γ Peg	Algenib	HIP 1067",
  "N27-Rev	रेवती	ξ Psc	xiPsc	HIP   8833",
  // "N27-Rev	रेवती	ε Psc	epsPsc	HIP 4906",
]
var $N27Feb20_delta = [  // alternates for few wrt to base set 
  "N06-Ard	आर्द्रा	α Ori	Betelgeuse	HIP  27989",
  //"N06-Ard	आर्द्रा	γ Gem	Alhena(Almeisan)	HIP 31681",
  "N10-Mag	मघाः	α Leo	Regulus	HIP  49669",
  //"N10-Mag	मघाः	ζ Leo	Adhafera	HIP 50335",

  "N18-Jye	ज्येष्ठा	α Sco	Antares	HIP  80763",
  // "N18-Jye	ज्येष्ठा	ε Sco	Larawag	HIP  82396",

  "N19-Mul	मूलं	λ Sco	Shaula	HIP  85927",
  // "N19-Mul	मूलं	κ Sco	Mula	HIP  86670",


  "N20-PAsh	पूर्वाषाढा	λ Sgr	Kaus Borealis	HIP  90496",
  // "N20-PAsh	पूर्वाषाढा	φ Sgr	Namalsadirah I	HIP 92041",

  "N21-UAsh	उत्तराषाढा	τ Sgr	xxx	HIP  93864",
  // "N21-UAsh	उत्तराषाढा	η Sgr	Hamalwarib(Arkab)	HIP  89462",
  // "N27-Rev	रेवती	ε Psc	epsPsc	HIP 4906",
]

var $NAshFix = [
  "N20-PAsh	पूर्वाषाढा	λ Sgr	Kaus Borealis	HIP 90496",
  "N21-UAsh	उत्तराषाढा	τ Sgr	Namalsadirah II	HIP 93864",	
]

var $NSensitivity = [
  "N22-Shr	धनिष्ठा	β Del	Rotanev	HIP 101769",
  "N23-Dha	धनिष्ठा	β Aqr	Sadalsuud	HIP 106278",
]

/*
Nakṣatra      |ConstituentStars         |YogaTara  
==============|=========================|=========
Aśvayuk       |(α,β) Ari                |β Ari
Bharaṇī       |(35,39,41) Ari           |41 Ari
Kṛttikā       |(17,19,20,23,27,η) Tau   |η Tau
Rohiṇī        |(α,γ,δ,ε,θ) Tau          |α Tau
Mṛgaśira      |(λ,θ1,θ2) Ori            |λ Ori
Ārdrā         |(α) Ori                  |γ Gem
Punarvasu     |(α,β) Gem (α,β) CMi      |β Gem
Puṣya         |(γ,δ,θ) Cnc              |δ Cnc
Āśleṣā        |(δ,ε,ζ,η,θ,σ) Hya        |ζ Hya
*Maghā         |(α,γ,ε,ρ,η,μ) Leo        |α Leo
P Phalgunī    |(δ,θ) Leo                |δ Leo
U Phalgunī    |(93,β) Leo               |β Leo
*Hasta         |(α,β,γ,δ,ε) Crv          |γ Crv
Citrā         |(α) Vir                  |α Vir
Svātī         |(α) Boo                  |α Boo
Viśākhā       |(α,β) Lib                |α Lib
Anūrādhā      |(β1,δ,π) Sco             |δ Sco
*Jyeṣṭhā       |(α,σ,τ) Sco              |α Sco
*Mūla          |(λ,ζ2,θ,ι1,κ,η,μ,ξ) Sco  |λ Sco
*P Aṣāḍhā      |(δ,ε) Sgr                |δ Sgr
*U Aṣāḍhā      |(ζ,σ) Sgr                |σ Sgr
Abhijit       |                         |α Aql
*Śravaṇa       |                         |β Del
*Dhaniṣṭhā     |                         |β Aqr
*Śatabhiṣak    |                         |α PsA
P Proṣṭapada  |(α,β) Peg                |α Peg
U Proṣṭapada  |(λ) Peg                  |λ Peg
*Revatī        |(ζ) Psc                  |ζ Psc
*/

var $NAbhyankar = [
  "N10-Mag	मघाः	α Leo	Regulus	HIP 49669",
  "N13-Has	हस्तः	γ Crv	Gienan	HIP  59803",
  "N18-Jye	ज्येष्ठा	α Sco	Antares	HIP  80763",
  "N19-Mul	मूलं	λ Sco	Shaula	HIP  85927",
  "N20-PAsh	पूर्वाषाढा	δ Sgr	Kaus Media	HIP 89931",
  "N21-UAsh	उत्तराषाढा	σ Sgr	Nunki	HIP 92855",	

  //"N22-Shr	धनिष्ठा	β Del	Rotanev	HIP 101769",  // Included in NSensitivity
  //"N23-Dha	धनिष्ठा	β Aqr	Sadalsuud	HIP 106278",

  "N24-Sha	शतभिषक्	α PsA	Fomalhaut	HIP 113368",
  "N27-Rev	रेवती	ζ Psc	Revati	HIP 5737",
]

var $N27Feb24 = [  // base set
  "N01-Ash	अश्विनी	β Ari	Sheratan	HIP 8903",
  "N02-Bha	भरणी	* 41 Ari	Bharani	HIP 13209",
  "N03-Kri	क्रित्तिकाः	η Tau	Alcyone	HIP 17702",
  "N04-Roh	रोहिणी	α Tau	Aldebaran	HIP  21421",
  "N05-Mrg	मृगशीर्षः	λ Ori	Meissa(Heka)	HIP  26207",
  "N06-Ard	आर्द्रा	γ Gem	Alhena(Almeisan)	HIP 31681",
  "N07-Pun	पुनर्वसू	β Gem	Pollux	HIP  37826",
  "N08-Pus	पुष्यः	δ Cnc	Asellus Australis	HIP  42911",
  "N09-Asl	आश्लेषः	ζ Hya	Minazal V	HIP 43813",
  "N10-Mag	मघाः	ζ Leo	Adhafera	HIP 50335",
  "N11-PPal	पूर्वफल्गुनी	δ Leo	Zosma	HIP  54872",
  "N12-UPal	उत्तरफल्गुनी	β Leo	Denebola	HIP  57632",
  "N13-Has	हस्तः	δ Crv	Algorab	HIP  60965",
  "N14-Chi	चित्रा	α Vir	Spica	HIP  65474",
  "N15-Swa	स्वाती	α Boo	Arcturus	HIP  69673",
  "N16-Vis	विशाखे	α2 Lib	Zubenelgenubi	HIP 72622",
  "N17-Anu	अनूराधा	δ Sco	Dschubba	HIP  78401",
  "N18-Jye	ज्येष्ठा	ε Sco	Larawag	HIP  82396",
  "N19-Mul	मूलं	κ Sco	Mula	HIP  86670",
  // "N20-PAsh	पूर्वाषाढा	φ Sgr	Namalsadirah I	HIP 92041",
  // "N21-UAsh	उत्तराषाढा	η Sgr	Hamalwarib(Arkab)	HIP  89462",
  "N20-PAsh	पूर्वाषाढा	λ Sgr	Kaus Borealis	HIP 90496",
  "N21-UAsh	उत्तराषाढा	τ Sgr	Namalsadirah II	HIP 93864",	
  "N22-Shr	श्रवणः	α Aql	Altair	HIP  97649",
  "N23-Dha	धनिष्ठा	β Del	Rotanev	HIP 101769",
  "N24-Sha	शतभिषक्	λ Aqr	Hydor	HIP 112961",
  "N25-PBha	पूर्वाभाद्रपदा	α Peg	Markab	HIP 113963",
  // "N26-UBha	उत्तराभाद्रपदा	λ Peg	Sadalnazi	HIP 112440",
  "N26-UBha	उत्तराभाद्रपदा	γ Peg	Algenib	HIP 1067",
  "N27-Rev	रेवती	ε Psc	epsPsc	HIP 4906",
]

var $N90 = [
  "N03-Kri	क्रित्तिकाः	* eta Tau	Alcyone	HIP 17702",
  "N03-Kri	क्रित्तिकाः	* 17 Tau	Electra	HIP 17499",
  "N03-Kri	क्रित्तिकाः	* 19 Tau	Taygeta	HIP 17531",
  "N03-Kri	क्रित्तिकाः	* 20 Tau	Maia	HIP 17573",
  "N03-Kri	क्रित्तिकाः	* 23 Tau	Merope	HIP 17608",
  "N03-Kri	क्रित्तिकाः	* 27 Tau	Atlas	HIP 17847",
  "N04-Roh	रोहिणी	* alf Tau	Aldebaran	HIP 21421",
  "N04-Roh	रोहिणी	* gam Tau	Prima Hyadum	HIP 20205",
  "N04-Roh	रोहिणी	* del Tau	Secunda Hyadum	HIP 20455",
  "N04-Roh	रोहिणी	* eps Tau	Ain	HIP 20889",
  "N04-Roh	रोहिणी	* tet2 Tau	Chamukuy	HIP 20894",
  "N06-Mrg	मृगशीर्षः	* alf Ori	Betelgeuse	HIP 27989",
  "N05-Mrg	मृगशीर्षः	* gam Ori	Bellatrix	HIP 25336",
  "N05-Mrg	मृगशीर्षः	* lam Ori	Heka	HIP 26207",
  "N06-Ard	आर्द्रा	* gam Gem	Alhena	HIP 31681",
  "N07-Pun	पुनर्वसू	* bet Gem	Pollux	HIP 37826",
  "N07-Pun	पुनर्वसू	* alf Gem	Castor	HIP 36850",
  "N08-Pus	पुष्यः	* del Cnc	Asellus Australis	HIP 42911",
  "N09-Asl	आश्लेषः	* del Hya	Minazal I	HIP 42313",
  "N09-Asl	आश्लेषः	* sig Hya	Minchir	HIP 42402",
  "N09-Asl	आश्लेषः	* eta Hya	Minazal II	HIP 42799",
  "N09-Asl	आश्लेषः	* eps Hya	Ashlesha	HIP 43109",
  "N09-Asl	आश्लेषः	* rho Hya	Minazal IV	HIP 43234",
  "N09-Asl	आश्लेषः	* zet Hya	Minazal V	HIP 43813",
  "N10-Mag	मघाः	* alf Leo	Regulus	HIP 49669",
  "N10-Mag	मघाः	* eps Leo	Algenubi	HIP 47908",
  "N10-Mag	मघाः	* mu Leo	Rasalas	HIP 48455",
  "N10-Mag	मघाः	* eta Leo	Al Jabah	HIP 49583",
  "N10-Mag	मघाः	* zet Leo	Adhafera	HIP 50335",
  "N10-Mag	मघाः	* gam Leo	Algieba	HIP 50583",
  "N11-PPal	पूर्वफल्गुनी	* del Leo	Zosma	HIP 54872",
  "N11-PPal	पूर्वफल्गुनी	* tet Leo	Chertan	HIP 54879",
  "N12-UPal	उत्तरफल्गुनी	* bet Leo	Denebola	HIP 57632",
  "N12-UPal	उत्तरफल्गुनी	* 93 Leo	93Leo	HIP 57565",
  "N13-Has	हस्तः	* del Crv	Algorab	HIP 60965",
  "N13-Has	हस्तः	* alf Crv	Alchiba	HIP 59199",
  "N13-Has	हस्तः	* eps Crv	Minkar	HIP 59316",
  "N13-Has	हस्तः	* gam Crv	Gienah	HIP 59803",
  "N13-Has	हस्तः	* bet Crv	Kraz	HIP 61359",
  "N14-Chi	चित्रा	* alf Vir	Spica	HIP 65474",
  "N15-Swa	स्वाती	* alf Boo	Arcturus	HIP 69673",
  "N16-Vis	विशाखे	* alf2 Lib	Zubenelgenubi	HIP 72622",
  "N16-Vis	विशाखे	* bet Lib	Zubeneschamali	HIP 74785",
  "N17-Anu	अनूराधा	* del Sco	Dschubba	HIP 78401",
  "N17-Anu	अनूराधा	* pi Sco	Fang	HIP 78265",
  "N17-Anu	अनूराधा	* bet Sco	Acrab	HIP 78820",
  "N17-Anu	अनूराधा	* ome1 Sco	Jabhat Acrabi I	HIP 78933",
  "N18-Jye	ज्येष्ठा	* alf Sco	Antares	HIP 80763",
  "N18-Jye	ज्येष्ठा	* eps Sco	Larawag	HIP 82396",
  "N18-Jye	ज्येष्ठा	* sig Sco	Alniyat	HIP 80112",
  "N18-Jye	ज्येष्ठा	* tau Sco	Alniyat II	HIP 81266",
  "N19-Mul	मूलं	* lam Sco	Shaula	HIP 85927",
  "N19-Mul	मूलं	* tet Sco	Sargas	HIP 86228",
  "N19-Mul	मूलं	* nu Sco	Lesath	HIP 85696",
  "N19-Mul	मूलं	* zet2 Sco	zet2Sco	HIP 82729",
  "N19-Mul	मूलं	* iot1 Sco	Girtab	HIP 87073",
  "N19-Mul	मूलं	* kap Sco	Mula	HIP 86670",
  "N20-PAsh	पूर्वाषाढा	* eps Sgr	Kaus Australis	HIP 90185",
  "N20-PAsh	पूर्वाषाढा	* gam Sgr	Alnasl	HIP 88635",
  "N20-PAsh	पूर्वाषाढा	* del Sgr	Kaus Media	HIP 89931",
  "N20-PAsh	पूर्वाषाढा	* lam Sgr	Kaus Borealis	HIP 90496",
  "N21-UAsh	उत्तराषाढा	* sig Sgr	Nunki	HIP 92855",
  "N21-UAsh	उत्तराषाढा	* phi Sgr	Namalsadirah I	HIP 92041",
  "N21-UAsh	उत्तराषाढा	* zet Sgr	Ascella	HIP 93506",
  "N21-UAsh	उत्तराषाढा	* tau Sgr	Namalsadirah II	HIP 93864",
  "N28-Abh	Abh	* alf Lyr	Vega	HIP 91262",
  "N28-Abh	Abh	* eps1 Lyr	Double Double I	HIP 91919",
  "N28-Abh	Abh	* zet1 Lyr	Nasr Alwaki	HIP 91971",
  "N22-Shr	श्रवणः	* alf Aql	Altair	HIP 97649",
  "N22-Shr	श्रवणः	* gam Aql	Tarazed	HIP 97278",
  "N22-Shr	श्रवणः	* bet Aql	Alshain	HIP 98036",
  "N23-Dha	धनिष्ठा	* alf Del	Sualocin	HIP 101958",
  "N23-Dha	धनिष्ठा	* eps Del	Aldulfin	HIP 101421",
  "N23-Dha	धनिष्ठा	* bet Del	Rotanev	HIP 101769",
  "N23-Dha	धनिष्ठा	* del Del	Al Ukud	HIP 102281",
  "N23-Dha	धनिष्ठा	* gam2 Del	Al Salib	HIP 102532",
  "N24-Sha	शतभिषक्	* lam Aqr	Hydor	HIP 112961",
  "N25-PBha	पूर्वाभाद्रपदा	* alf Peg	Markab	HIP 113963",
  "N25-PBha	पूर्वाभाद्रपदा	* bet Peg	Scheat	HIP 113881",
  "N26-UBha	उत्तराभाद्रपदा	* alf And	Alpheratz	HIP 677",
  "N26-UBha	उत्तराभाद्रपदा	* gam Peg	Algenib	HIP 1067",
  // "N26-UBha	उत्तराभाद्रपदा	* lam Peg	Sadalnazi	HIP 112440",
  "N27-Rev	रेवती	* alf Psc	Alrescha	HIP 9487",
  "N27-Rev	रेवती	* eps Psc	epsPsc	HIP 4906",
  "N01-Ash	अश्विनी	* alf Ari	Hamal	HIP 9884",
  "N01-Ash	अश्विनी	* bet Ari	Sheratan	HIP 8903",
  "N01-Ash	अश्विनी	* gam Ari	Mesarthim	HIP 8832",
  "N02-Bha	भरणी	* 41 Ari	Bharani	HIP 13209",
  "N02-Bha	भरणी	* 31 Ari	31Ari	HIP 12153",
  "N02-Bha	भरणी	* 35 Ari	Barani II	HIP 12719",
]


var $N12 = [  // base set
  "M01-Rev	रेवती	ε Psc	epsPsc	HIP 4906",
  "M02-Bha	भरणी	* 41 Ari	Bharani	HIP 13209",
  "M03-Mrg	मृगशीर्षः	λ Ori	Meissa(Heka)	HIP  26207",
  "M04-Pun	पुनर्वसू	β Gem	Pollux	HIP  37826",
  "M05-Mag	मघाः	α Leo	Regulus	HIP 49669",
  "M06-PPal	पूर्वफल्गुनी	δ Leo	Zosma	HIP  54872",
  "M07-Chi	चित्रा	α Vir	Spica	HIP  65474",
  "M08-Vis	विशाखे	α2 Lib	Zubenelgenubi	HIP 72622",
  "M09-Jye	ज्येष्ठा	α Sco	Antares	HIP  80763",
  "M10-PAsh	पूर्वाषाढा	λ Sgr	Kaus Borealis	HIP 90496",
  "M11-Dha	धनिष्ठा	β Del	Rotanev	HIP 101769",
  "M12-PBha	पूर्वाभाद्रपदा	α Peg	Markab	HIP 113963",
]

var $N83 = [ //VGJ
  "N01-Ash	अश्विनी	β Ari	Sheratan	HIP 8903",
  "N01-Ash	अश्विनी	α Ari	Hamal	HIP 9884",
  "N01-Ash	अश्विनी	γ Ari	Mesarthim	HIP 8832",
  "N02-Bha	भरणी	* 41 Ari	Bharani	HIP 13209",
  // "N02-Bha	भरणी	* 31 Ari	31Ari	HIP 12153",
  "N02-Bha	भरणी	* 39 Ari	39Ari	HIP 13061",
  "N02-Bha	भरणी	* 35 Ari	Barani II	HIP 12719",
  "N03-Kri	क्रित्तिका	η Tau	Alcyone	HIP 17702",
  "N03-Kri	क्रित्तिका	* 17 Tau	Electra	HIP 17499",
  "N03-Kri	क्रित्तिका	* 19 Tau	Taygeta	HIP 17531",
  "N03-Kri	क्रित्तिका	* 20 Tau	Maia	HIP 17573",
  "N03-Kri	क्रित्तिका	* 23 Tau	Merope	HIP 17608",
  "N03-Kri	क्रित्तिका	* 27 Tau	Atlas	HIP 17847",
  "N04-Roh	रोहिणी	α Tau	Aldebaran	HIP 21421",
  "N04-Roh	रोहिणी	γ Tau	Prima Hyadum	HIP 20205",
  "N04-Roh	रोहिणी	δ1 Tau	Secunda Hyadum	HIP 20455",
  "N04-Roh	रोहिणी	ε Tau	Ain	HIP 20889",
  "N04-Roh	रोहिणी	θ2 Tau	Chamukuy	HIP 20894",
  "N05-Mrg	मृगशीर्ष	λ Ori	Meissa(Heka)	HIP 26207",
  "N05-Mrg	मृगशीर्ष	γ Ori	Bellatrix	HIP 25336",
  "N05-Mrg	मृगशीर्ष	α Ori	Heka	HIP 27989",
  "N06-Ard	आर्द्रा	γ Gem	Alhena(Almeisan)	HIP 31681",
  "N07-Pun	पुनर्वसू	β Gem	Pollux	HIP 37826",
  "N07-Pun	पुनर्वसू	α Gem	Castor	HIP 36850",
  "N08-Pus	पुष्य	δ Cnc	Asellus Australis	HIP 42911",
  "N09-Asl	आश्लेषा	ζ Hya	Minazal V	HIP 43813",
  "N09-Asl	आश्लेषा	δ Hya	Minazal I	HIP 42313",
  "N09-Asl	आश्लेषा	ε Hya	Ashlesha	HIP 43109",
  "N09-Asl	आश्लेषा	η Hya	Minazal II	HIP 42799",
  "N09-Asl	आश्लेषा	ρ Hya	Minazal IV	HIP 43234",
  "N09-Asl	आश्लेषा	σ Hya	Minchir	HIP 42402",
  "N10-Mag	मघा	ζ Leo	Adhafera	HIP 50335",
  "N10-Mag	मघा	α Leo	Regulus	HIP 49669",
  "N10-Mag	मघा	γ1 Leo	Algieba	HIP 50583",
  "N10-Mag	मघा	ε Leo	Algenubi	HIP 47908",
  "N10-Mag	मघा	η Leo	Al Jabah	HIP 49583",
  "N10-Mag	मघा	μ Leo	Rasalas	HIP 48455",
  "N11-PPal	पूर्वफल्गुनी	δ Leo	Zosma	HIP 54872",
  "N11-PPal	पूर्वफल्गुनी	θ Leo	Chertan	HIP 54879",
  "N12-UPal	उत्तरफल्गुनी	β Leo	Denebola	HIP 57632",
  "N12-UPal	उत्तरफल्गुनी	* 93 Leo	93Leo	HIP 57565",
  "N13-Has	हस्त	δ Crv	Algorab	HIP 60965",
  "N13-Has	हस्त	α Crv	Alchiba	HIP 59199",
  "N13-Has	हस्त	β Crv	Kraz	HIP 61359",
  "N13-Has	हस्त	γ Crv	Gienah	HIP 59803",
  "N13-Has	हस्त	ε Crv	Minkar	HIP 59316",
  "N14-Chi	चित्रा	α Vir	Spica	HIP 65474",
  "N15-Swa	स्वाती	α Boo	Arcturus	HIP 69673",
  "N16-Vis	विशाखे	α2 Lib	Zubenelgenubi	HIP 72622",
  "N16-Vis	विशाखे	α1 Lib	Zubenelgenubi II	HIP 72603",
  "N17-Anu	अनूराधा	δ Sco	Dschubba	HIP 78401",
  "N17-Anu	अनूराधा	β1 Sco	Acrab	HIP 78820",
  "N17-Anu	अनूराधा	π Sco	Fang	HIP 78265",
  "N17-Anu	अनूराधा	ω1 Sco	Jabhat Acrabi I	HIP 78933",
  "N18-Jye	ज्येष्ठा	ε Sco	Larawag	HIP 82396",
  "N18-Jye	ज्येष्ठा	α Sco	Antares	HIP 80763",
  "N18-Jye	ज्येष्ठा	σ Sco	Alniyat	HIP 80112",
  "N19-Mul	मूल	κ Sco	Mula	HIP 86670",
  "N19-Mul	मूल	ζ2 Sco	zet2Sco	HIP 82729",
  "N19-Mul	मूल	θ Sco	Sargas	HIP 86228",
  "N19-Mul	मूल	ι1 Sco	Girtab	HIP 87073",
  "N19-Mul	मूल	λ Sco	Shaula	HIP 85927",
  "N19-Mul	मूल	ν Sco	Lesath	HIP 85696",
  "N20-PAsh	पूर्वाषाढा	λ Sgr	Kaus Borealis	HIP 90496",
  "N20-PAsh	पूर्वाषाढा	γ Sgr	Alnasl	HIP 88635",
  "N20-PAsh	पूर्वाषाढा	δ Sgr	Kaus Media	HIP 89931",
  "N20-PAsh	पूर्वाषाढा	ε Sgr	Kaus Australis	HIP 90185",
  "N21-UAsh	उत्तराषाढा	τ Sgr	Namalsadirah II	HIP 93864",
  "N21-UAsh	उत्तराषाढा	ζ Sgr	Ascella	HIP 93506",
  "N21-UAsh	उत्तराषाढा	σ Sgr	Nunki	HIP 92855",
  "N21-UAsh	उत्तराषाढा	φ Sgr	Namalsadirah I	HIP 92041",
  "N22-Shr	श्रवण	α Aql	Altair	HIP 97649",
  "N22-Shr	श्रवण	β Aql	Alshain	HIP 98036",
  "N22-Shr	श्रवण	γ Aql	Tarazed	HIP 97278",
  "N23-Dha	धनिष्ठा	β Del	Rotanev	HIP 101769",
  "N23-Dha	धनिष्ठा	α Del	Sualocin	HIP 101958",
  "N23-Dha	धनिष्ठा	γ2 Del	Al Salib	HIP 102532",
  "N23-Dha	धनिष्ठा	δ Del	Al Ukud	HIP 102281",
  "N24-Sha	शतभिषक्	λ Aqr	Hydor	HIP 112961",
  "N25-PBha	पूर्वाभाद्रपदा	α Peg	Markab	HIP 113963",
  "N25-PBha	पूर्वाभाद्रपदा	β Peg	Scheat	HIP 113881",
  // "N26-UBha	उत्तराभाद्रपदा	λ Peg	Sadalnazi	HIP 112440",
  "N26-UBha	उत्तराभाद्रपदा	α And	Alpheratz	HIP 677",
  "N26-UBha	उत्तराभाद्रपदा	γ Peg	Algenib	HIP 1067",
  "N27-Rev	रेवती	ε Psc	epsPsc	HIP 4906"
]

$N_VGJ = $N83

$N_BELELGEUSE = [
  "N05-Mrg	मृगशीर्ष	α Ori	Heka	HIP 27989"
]

$N_39Ari = [
  "N02-Bha	भरणी	* 39 Ari	39Ari	HIP 13061"
]

/*
1. I am selecting the stars to represent the half-divisions mentioned in PT and VGJ. 
Ardra-->gama Gem (as per abhyankar). 
Aslesha-->zeta hya;   
Magha-->zeta leo; 
hasta--> delta crv;  
Jyestha--> epsilon sco.  
Mula--> k sco  
P.ashadha-->phi sgr  
U.asha-->eta sgr 
Revati-->epsilon psc;  
This is called Baahuu (that is hand in the vedas) Gemini stars fit with this image.
*/

function GetNaksLatLonSimple($naks, $jd) {
  var $naks_map = $naks
  .map(function (v) { return v.split("\t") })
  .map(function (v) {
    var h = {}
    v.map(function (e, i) {
      h[header_naks[i]] = e //.replace(/HIP\s+/,'')
    })
    return h
  }).map(function (v) {
    v.hip = v.hip.replace(/\s*\D+\s*$/, '')
    return v
  })

  if ($jd === undefined) $jd = 1501914.5  // 600-1-1 BCE
  // say(['nid', 'naks', 'gname', 'lon', 'lat', 'ra', 'dec','size', 'mag', 'year', 'date', 'jd'].join("\t")) 
  //nid	naks	gname	lon	lat	year	date	jd
  //say(['nid', 'naks', 'gname', 'lon', 'lat', 'ra', 'dec', 'year', 'date', 'jd'].join("\t")) 
  say(['nid', 'naks', 'gname', 'lon', 'lat', 
      //'ra', 'dec', 
      'year', 'date', 'jd'].join("\t")) 
  JD($jd)
  var dt = DT()
  var yy = dt.replace(/......T.*/, "")*1
  var ans = []
  $naks_map.forEach(function (e) {
    var o = core.getObjectInfo(e.hip); W(1)
    if (!e.naks) e.naks = e.nid
    var info = [e.nid, e.naks, e.gname, 
      o.elong.toFixed(3), o.elat.toFixed(3), 
      //o.ra.toFixed(3), o.dec.toFixed(3), 
      // o.size.toFixed(3), o.vmag.toFixed(3), 
      // o['size-deg'], o.vmag.toFixed(3), 
      yy, dt, $jd].join("\t")
    ans.push(info)
    say(info)
  })
  return ans
}

// ddump (n89[0], "pretty")
$GRUHAS2 = [
  "P01-Sur	सूर्य	Sun	Sun	Sun",
  "P02-Cha	चन्द्र	Moon	Moon	Moon",
  "P03-Ang	मंगळ	Mars	Mars	Mars",
  "P04-Bud	बुध	Mercury	Mercury	Mercury",
  "P05-Bri	गुरु	Jupiter	Jupiter	Jupiter",
  "P06-Shu	शुक्र	Venus	Venus	Venus",
  "P07-Sha	सूर्य	Saturn	Saturn	Saturn",
]

$GRUHAS_MARS = [
  "P01-Sur	सूर्य	Sun	Sun	Sun",
  "P03-Ang	मंगळ	Mars	Mars	Mars",
]

var header_gruha = "gid	gruha	name".toLowerCase().split(/\t/)
function GetGruhaLatLonSimple($gruhas, $jd, $printHeader) {
  var $gruhas_map = $gruhas
  .map(function (v) { return v.split("\t") })
  .map(function (v) {
    var h = {}
    v.map(function (e, i) {
      h[header_gruha[i]] = e //.replace(/HIP\s+/,'')
    })
    return h
  }).map(function (v) {
    // v.hip = v.hip.replace(/\s*\D+\s*$/, '')
    return v
  })

  if ($jd === undefined) $jd = 1501914.5  // 600-1-1 BCE
  // say(['nid', 'naks', 'gname', 'lon', 'lat', 'ra', 'dec','size', 'mag', 'year', 'date', 'jd'].join("\t")) 
  if ($printHeader) say(['gid', 'gruha', 'name', 'lon', 'lat', 'ra', 'dec', 'elongation', 'alt', 'ymd', 'date', 'jd'].join("\t")) 
  JD($jd)
  var dt = DT()
  var yymmdd = dt.replace(/T.*/, "")
  var ans = []
  $gruhas_map.forEach(function (e) {
    var o = core.getObjectInfo(e.name); W(1)
    if (!('elongation' in o )) o.elongation= 0
    var info = [e.gid, e.gruha, e.name,
      o.elong.toFixed(3), o.elat.toFixed(3), 
      o.ra.toFixed(3), o.dec.toFixed(3), o.elongation.toFixed(3), o.altitude.toFixed(3),
      // o.size.toFixed(3), o.vmag.toFixed(3), 
      // o['size-deg'], o.vmag.toFixed(3), 
      yymmdd, dt, $jd].join("\t")
    ans.push(info)
    say(info)
  })
  return ans
}


// GetN89LatLong($JD_0 - 3400*365, 1000, 3)
// GetN89LatLong($JD_0 - 2500*365, 1000, 3)
// GetN89LatLong($JD_0 - 1500*365, 1000, 3)

$GetInfoTemplate = {
  "above-horizon": false,
  "absolute-mag": -2.610257625579834,
  "airmass": 1.2045358419418335,
  "altitude": -64.18340465466943,
  "altitude-geometric": -64.18340465466943,
  "appSidTm": "13h38m30.6s",
  "azimuth": 34.09949281089747,
  "azimuth-geometric": 34.09949281089747,
  "bV": -0.09055119752883911,
  "dec": 8.588860931242447,
  "decJ2000": 24.149290180920378,
  "distance-ly": 403.1599229877891,
  "elat": 3.717908070386358,
  "elatJ2000": 4.097311727653709,
  "elong": 12.889319392798896,
  "elongJ2000": 59.9874110027904,
  "found": true,
  "glat": -23.432673802197694,
  "glong": 166.62377110972253,
  "hourAngle-dd": 194.29530564121666,
  "hourAngle-hms": "12h57m10.9s",
  "iauConstellation": "Tau",
  "localized-name": "",
  "meanSidTm": "13h38m30.6s",
  "name": "HIP 17702",
  "parallax": 0.00809,
  "ra": 10.332347977359342,
  "raJ2000": 56.85476541294855,
  "rise": "4h56m",
  "rise-dhr": 4.927521705627441,
  "set": "17h14m",
  "set-dhr": 17.226945877075195,
  "sglat": -29.3029646878894,
  "sglong": -23.368942730969668,
  "size": 0,
  "size-dd": 0,
  "size-deg": "+0.00000°",
  "size-dms": "+0°00'00.00\"",
  "spectral-class": "B7III",
  "star-type": "double-star",
  "transit": "11h05m",
  "transit-dhr": 11.077234268188477,
  "type": "Star",
  "variable-star": "no",
  "vmag": 2.8499999046325684,
  "vmage": 2.8499999046325684,
  "wds-position-angle": 290.1000061035156,
  "wds-separation": 117.31199645996094,
  "wds-year": 2011,
  "jd": 1210557.284468
}

var $PLANET_INFO_TEMPLATE = {
"above-horizon": true,
"airmass": 1.0669883489608765,
"altitude": 69.58924102783203,
"altitude-geometric": 69.58301370225458,
"appSidTm": "7h54m08.2s",
"azimuth": 306.95923690234025,
"azimuth-geometric": 306.95923690234025,
"dec": 24.50447200351985,
"decJ2000": 24.52505977041081,
"distance": 2.088307108418237,
"elat": 1.4282507886787779,
"elatJ2000": 1.4247602670878907,
"elong": 99.72480222312056,
"elongJ2000": 99.43136759026238,
"elongation": 0.8843803832336223,
"elongation-deg": "+50.6713°",
"elongation-dms": "+50°40'17\"",
"found": true,
"glat": 8.867583598743906,
"glong": -170.15383814285963,
"heliocentric-velocity": "[-0.0105339, -0.00738066, 0.000103731]",
"heliocentric-velocity-kms": "22.27109",
"hourAngle-dd": 17.839169844227968,
"hourAngle-hms": "1h11m21.4s",
"iauConstellation": "Gem",
"illumination": 94.01056671142578,
"localized-name": "मंगळ",
"meanSidTm": "7h54m09.3s",
"name": "Mars",
"parallacticAngle": 121.15975579999404,
"phase": 0.940105676651001,
"phase-angle": 0.4944888567162582,
"phase-angle-deg": "+28.3321°",
"phase-angle-dms": "+28°19'56\"",
"ra": 100.6948836272234,
"raJ2000": 100.37328288489253,
"rise": "9h27m",
"rise-dhr": 9.450689315795898,
"scale": 1,
"set": "22h17m",
"set-dhr": 22.28936004638672,
"sglat": -49.63098717510823,
"sglong": 21.698911129470268,
"size": 0.000021742199405062665,
"size-dd": 0.00124573626324194,
"size-deg": "+0.00125°",
"size-dms": "+0°00'04.48\"",
"transit": "15h52m",
"transit-dhr": 15.870025634765625,
"type": "planet",
"velocity": "[-0.0105339, -0.00738066, 0.000103731]",
"velocity-kms": "22.27109",
"vmag": 1.6138644218444824,
"vmage": 1.6138644218444824
}

// var $NAKSHATRA_LIST = [
//   //'#,नक्षत्रम्,राशिः,Star,HIPId',
//   'N01,अश्विनी,मेषः,Hamal,9884,Ashwini',
//   'N02,भरणी,मेषः,Bharani,13209,Bharani',
//   'N03,कृत्तिका,वृषभः,Alcyone,17702,Krittika',
//   'N04,रोहिणी,वृषभः,Aldebaran,21421,Rohini',
//   'N05,मृगशीर्षा,मिथुनः,Meissa,26207,Mrigashirisham',
//   'N06,आर्द्रा,मिथुनः,Betelgeuse,27989,Thiruvadarai',
//   'N07,पुनर्वसू (द्वि),मिथुनः,Pollux,37826,Punarpasu',
//   'N08,पुष्या;तिष्या,कर्कः,Asellus Australis,42911,Pushyam',
//   //'N09,आश्लेषा,कर्कः,Minchir,42402,Ayilyam',
//   'N09,आश्लेषा,कर्कः,Minazal V,43813,Ayilyam',
//   'N10,मघा,सिंहः,Regulus,49669,Makam',
//   'N11,पूर्वफल्गुनी,सिंहः,Zozma,54872,Pooram',
//   //'N12,उत्तरफल्गुनी,कन्या,Zozma,54872,Uttiram',
//   'N12,उत्तरफल्गुनी,कन्या,Cheratan,54879,Uttiram',
//   'N13,हस्ता,कन्या,Algorab,60965,Hastam',
//   'N14,चित्रा,कन्या,Spica,65474,Chitrai',
//   'N15,स्वाती,तुला,Arcturus,69673,Swati',
//   'N16,विशाखा,तुला,Zubenelgenubi,72603,Vishakam',
//   'N17,अनुराधा,वृश्चिका,Dschubba,78401,Anusham',
//   'N18,ज्येष्ठा,वृश्चिका,Antares,80763,Kettai',
//   'N19,मूला,धनुः,Shaula,85927,Moolam',
//   'N20,पूर्व्वाषाढा,धनुः,Kaus Australis,90185,Pooradam',
//   'N21,उत्तराषाढा,धनुः,Nunki,92855,Uttiradam',
//   'N22,श्रवणा,मकरः,Altair,97649,Thiruvonam',
//   //'N23,धनिष्ठा,मकरः,Fomalhaut,113368,Avittam',
//   'N23,धनिष्ठा,मकरः,Sualocin,101958,Avittam',
//   'N24,शतभिषक्,कुम्भः,Situla,111710,Shatayam',
//   'N25,पूर्वभाद्रपदा,कुम्भः,Markab,113963,Poorattadi',
//   'N26,उत्तरभाद्रपदा,मीना,Alpheratz,677,Uttiratadi',
//   'N27,रेवती,मीना,Alrischa,9487,Revati',
//   'N28,अभिजित्,मकरः,Vega,91262,Abhijit',
//   // 'N29,उत्तरा,,Denebola,57632,Uttara',
// ];

// var $NAKSHATRAS = [];
// for (i in $NAKSHATRA_LIST) {
//   var items = $NAKSHATRA_LIST[i].split(/,/);
//   var nid = items[0];
//   var tara = items[1];
//   var rasi = items[2];
//   var star = items[3];
//   var hip = 'HIP ' + items[4];
//   var naks = items[5];

//   $NAKSHATRAS.push({ nid: nid, tara: tara, rasi: rasi, star: star, hip: hip, naks: naks });
// }

function naks_array(n) {
  return n.map(
    function (x) {
      return (x.split("\n")[0]).split("\t")
    })
}

var $N83A = naks_array($N83)
function RND(n, d) {
  // if (d == undefined) d = 2
  return Math.round(n * Math.pow(10, d)) / Math.pow(10, d)
  // return Math.round(n,d)
}
function R2(n) { return RND(n, 2) }

// say("Here is the array of arrays of the Naksatra data")

function diff_angle(a, b) {
  var d = b-a;
  if (d < -180) d += 360;
  if (d > 180) d -= 360;
  return d;
}