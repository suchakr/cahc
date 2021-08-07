# %%
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from sympy import *
import re

#%%
'''
पलानि पंचादशदपां धृतानि तदाढकं द्रोणमतः प्रमेयम्। 
त्रिभिर्विहीनं कुडवैस्तु कार्यं तन्नाडिकायास्तु भवेत् प्रमाणम्॥ ऋ २४॥ 

कला दश सविंशा स्याद् द्वे मुहुर्तस्य नाडिके। 
द्युस्त्रिंशंत् तत्कलानां तु षट्शती त्र्यधिका भवेत्॥ ऋ १६ ,य ३८॥

नाडिके द्वे मुहुर्तस्तु पंचाशत्पलमाढकम्। 
आढकात्कुम्भको द्रोणः कुटपैर्वर्धते त्रिभिः॥य १७॥

द्युहेयं पर्व चेत्पादे पादस्त्रिंशत्तु सैकिका। 
भागात्मनापवृज्यांशान् निर्दिशेदधिको यदि॥य १२॥

पंचत्रिंशं शतं पौष्णम् एकोनमयनोन्यृषेः। 
पर्वणां स्याच्चतुष्पादी काष्ठानां चैव ताः कलाः॥य ३०॥


'''

# https://www.transliteral.org/pages/z140124011449/view
'''
याजुषज्योतिषम्

पञ्चसंवत्सरमयं युगाध्यक्षं प्रजापतिम् | दिनर्त्वयनमासाङ्गं प्रणम्य शिरसा शुचिः ॥१॥
ज्योतिषामयनं पुण्यं प्रवक्ष्याम्यनुपूर्वशः | विप्राणां सम्मतं लोके यज्ञकालार्थ सिद्धये ॥२॥
वेद हि यज्ञार्थमभिप्रवृत्ताः कालानुपूर्व्या विहिताश्च यज्ञाः | तस्मादिदं कालविधानशास्त्रं यो ज्योतिषं वेद स वेद यज्ञान् ॥३॥
यथा शिखा मयूराणां नागानां मणयो यथा | तद्वद्वेदाङ्गशास्त्राणां ज्यौतिषं मूर्धानि स्थितम् ॥४॥
ये बृहस्पतिना भुक्ता मीनात्प्रभृति राशयः | ते हृताः पञ्चभिर्भूता यः शेषः स परिग्रहः ॥०॥
माघशुक्लप्रपन्नस्य पौषकृष्णसमापिनः | युगस्य पञ्चवर्षस्य कालज्ञानं प्रचक्षते ॥५॥
स्वराक्रमेते सोमार्कौ यदा साकं सवासवौ | स्यात्तदादियुगं माघस्तपः शुक्लोऽयनं ह्युदक् ॥६॥
प्रपद्यते श्रविष्ठादौ सूर्याचन्द्रमसावुदक् | सार्पार्धे दक्षिणार्कस्तु माघश्रावणयोः सदा ॥७॥
धर्मवृद्धिरपां प्रस्थः क्षपाह्रास उदग्गतौ | दक्षिणे तौ विपर्यासः षण्मुहूर्त्ययनेन तु ॥८॥
प्रथमं सप्तमं चाहुरयनाद्यं त्रयोदशम् | चतुर्थं दशमं चैव द्विर्युग्मं बहुलेप्यृतौ ॥९॥
वसुस्त्वष्टा भवोऽजश्च मित्रः सर्पोऽश्विनौ जलम् | धाता कश्चायनाद्याः स्युरर्धपञ्चमभस्त्वृतुः ॥१०॥
एकान्तरेऽह्नि मासे च पूर्वान् कृत्वादिमुत्तरः | अर्धयोः पञ्चवर्षाणामृदु पञ्चदशाष्टमौ ॥११॥
द्युहेयं पर्व चेत्पादे पादस्त्रिंशत्तु सैकिका | भागात्मनापवृज्यांशान् निर्दिशेदधिको यदि ॥१२॥
निरेकं द्वादशाभ्यस्तं द्विगुणं गतसञ्ज्ञिकम् | षष्ट्या षष्ट्या युतं द्वाभ्यां पर्वणां राशिरुच्यते ॥१३॥
स्युः पादोऽर्धन्त्रिपाद्याया त्रिद्वयेकऽह्नः कृतस्थितिम् | साम्येन्दोस्तृणोऽन्ये तु पर्वकाः पञ्च सम्मिताः ॥१४॥
भांशाः स्युरष्टकाः कार्याः पक्षद्वादशकोद्गताः | एकादशगुणश्चोनः शुक्लेऽर्धं चैन्दवा यदि ॥१५॥
नवकैरुद्गतोंशः स्यादूनः सप्तगुणो भवेत् | आवापस्त्वयुजेऽर्धं स्यात्पौलस्ये.आस्तङ्गतेऽपरम् ॥१६॥
जावाद्यंशैः समं विद्यात् पूर्वार्धे पर्व सूत्तरे | भादानं स्याच्चतुर्दश्यां काष्ठानां देविना कलाः ॥१७॥
जौ द्रा गः खे श्वे ही रो षा श्चिन्मूषक्ण्यः सूमाधाणः | रे मृ घाः स्वापोजः कृष्यो ह ज्येष्ठा इत्यृक्षा लिङ्गैः ॥१८॥
कार्या भांशाष्टकास्थाने कला एकान्नविंशतिः | उनस्थाने त्रिसप्तति मुद्ववपेदूनसम्भवे ॥१९॥
तिथिमेकादशाभ्यस्तां पर्वभांशसमन्विताम् | विभज्य भसमूहेन तिथिनक्षत्रमादिशेत् ॥२०॥
याः पर्वाभादानकलास्तासु सप्तगुणां तिथिम् | युक्त्या तासां विजानीयात् तिथिभादानिकाः कलाः ॥२१॥
अतीतपर्वभागेभ्यः शोधयेद् द्विगुणां तिथिम् | तेषु मण्डलभागेषु तिथिनिष्ठाङ्गतो रविः ॥२२॥
विषुवन्तं द्विरभ्यस्तं रूपोनं षड्गुणीकृतम् | पक्षा यदर्धं पक्षाणां तिथिः स विषुवान् स्मृतः ॥२३॥
पलानि पञ्चाशदपां धृतानि तदाढकं द्रोणमतः प्रमेयम् | त्रिभिर्विहीनं कुड्वैस्तु कार्यं तन्नाडिकायास्तु भवेत् प्रमाणम् ॥२४॥
एकादशभिरभ्यस्य पर्वाणि नवभिस्तिथिम् | युगलब्धं सपर्व स्याद् वर्तमानार्कभं क्रमात् ॥२५॥
सूर्यर्क्षभागान् नवभिर्विभज्य शेषान् द्विरभ्यस्य दिनोपभुक्तिः | तिथेर्युता भुक्तिदिनेषु कालो योगो दिनैकादशकेन् तद्भम् ॥२६॥
त्र्यंशो भशेषो दिवसांशभागश्चतुर्दशस्याप्यपनीय भिन्नम् | भार्धेऽधिके चाधिगते परोंऽशोद्वावुत्तमे तन्नवकैरवेत्य ॥२७॥
त्रिंशत्यह्नां सषट्षष्टिरब्दः षट् चर्तवोऽयने | मासा द्वादश सौर्याः स्युरेतत् पञ्चगुणं युगम् ॥२८॥
उदयावासवस्य स्युर्दिनराशि सपञ्चकः | ऋषेर्द्विषष्टिहीनः स्याद् विंशत्या चैकयास्तृणाम् ॥२९॥
पञ्चत्रिंशं शतं पौष्णम् एकोनमयनोन्यृषेः | पर्वणां स्याच्चतुष्पादी काष्ठानां चैव ताः कलाः ॥३०॥
सावनेन्दुस्तृमासानां षष्टिः सैकद्विसप्तिका | द्युस्त्रिंशत् सावनः सार्धः सौरस्तृणां स पर्ययः ॥३१॥
अग्निः प्रजापतिः सोमो रुद्रोदितिबृहस्पती | सर्पाश्च पितरश्चैव भगश्चैवार्यमापि च ॥३२॥
सविता त्वष्टाथ वायुश्चेन्द्राग्नी मित्र एव च | इन्द्रो निॠतिरापो वै विश्वेदेवास्तथैव च ॥३३॥
विष्णुर्वसवो वरुणोओऽजेकपात् तथैव च | अहिर्बुध्न्यस्तथा पूषा अश्विनौ यम एव च ॥३४॥
नक्षत्रदेवता एता एताभिर्यज्ञकर्मणि | यजमानस्य शास्त्रज्ञैर्नाम नक्षत्रजं स्मृतम् ॥३५॥
उग्राण्यार्द्रा च चित्रा च विशाखा श्रवणोश्वयुक् | क्रूरणि तु मघास्वाती ज्येष्टा मूलं यमस्य च ॥३६॥
द्यूनं द्विषष्टिभागेन ज्ञे (हे)यं सौरं सपार्वणम् | यत्कृतावुपजायेते मध्येऽन्ते चाधिमासकौ ॥३७॥
कला दश सविंशा स्याद् द्वे मुहुर्तस्य नाडिके | द्युस्त्रिंशत् तत्कलानां तु षट्शती त्र्यधिका भवेत् ॥३८॥
ससप्तमं भयुक् सोमः सूर्यो द्यूनि त्रयोदश | नवमानि तु पञ्चाह्नः काष्ठा पञ्चाक्षरा भवेत् ॥३९॥
यदुत्तरस्यायनतो गतं स्याच् छेषं तथा दक्षिणतोऽयनस्य | तदेकषष्ट्याद्विगुणं विभक्तं सद्वादशं स्याद् दिवसप्रमाणम् ॥४०॥
यदर्धं दिनभागानां सदा पर्वणि पर्वणि | ॠतुशेषं तु तद् विद्यात् सङ्ख्याय सह सर्वणाम् ॥४१॥
इत्युपायसमुद्देशो भूयोप्यह्नः प्रकल्पयेत् | ज्ञेयराशिं गताभ्यस्तं विभजेज्ज्ञानराशिना ॥४२॥
इत्येतन्मासवर्षाणां मुहूर्तोदयपर्वणाम् | दिनर्त्वयनमासाङ्गं व्याख्यानं लगधोऽब्रवीत् ॥००॥
सोमसूर्यस्तृचरितं विद्वान् वेदविदश्नुते | सोमसूर्यस्तृचरितं लोकं लोके च सम्मतिम् ॥४३॥

॥इति याजुषज्योतिषं समाप्तम् ॥

'''

''

#%%

# (पलम्, आढक, द्रोण, कुडव, नाडिका, मुहुर्त, कुम्भक, कुटप, minutes, hours, days) 
syms = symbols(
  'पलम् आढक द्रोण_कुम्भक कुडव_कुटप नाडिका' +
  ' मुहुर्त कला काष्ठा'+
  ' युग पर्व चान्द्रायन भागा अंश_भांश नक्षत्रम्' + 
  ' गुर्वाक्षर सौरृतु सौरायन अब्दः' +
  ' सौरमासः चान्द्रमासः स्तृमासः' +
  ' minutes hours द्युः'
  )

(पलम्,आढक,द्रोण_कुम्भक,कुडव_कुटप,नाडिका,
 मुहुर्त,कला,काष्ठा,
 युग,पर्व,चान्द्रायन,भागा,अंश_भांश,नक्षत्रम्,
 गुर्वाक्षर,सौरृतु,सौरायन,अब्दः,
 सौरमासः,चान्द्रमासः,स्तृमासः,
 minutes, hours, द्युः) = syms

# %%
dfs=[]
for sym in syms :
  print(sym)
  ans = pd.DataFrame(solve([
  # पलानि पंचादशदपां धृतानि तदाढकं द्रोणमतः प्रमेयम्। 
  # त्रिभिर्विहीनं कुडवैस्तु कार्यं तन्नाडिकायास्तु भवेत् प्रमाणम्॥ ऋ २४॥ 
    आढक - पलम्/50,    # ऋ २४ , य १७
    द्रोण_कुम्भक - आढक/4 ,     # ऋ २४
    नाडिका - द्रोण_कुम्भक-3*कुडव_कुटप, # ऋ २४, य १७
    आढक - कुडव_कुटप/16,    # ऋ २४ 

  # नाडिके द्वे मुहुर्तस्तु पंचाशत्पलमाढकम्। 
  # आढकात्कुम्भको द्रोणः कुटपैर्वर्धते त्रिभिः॥य १७॥
    मुहुर्त - नाडिका/2,  # य १७ ऋ १६ ,य ३८
    # कुम्भक - द्रोण,    # य १७
    # कुटप - कुडव,    # य १७

  # कला दश सविंशा स्याद् द्वे मुहुर्तस्य नाडिके। 
  # द्युस्त्रिंशंत् तत्कलानां तु षट्शती त्र्यधिका भवेत्॥ ऋ १६ ,य ३८॥
    नाडिका - कला/(10+1/20), #ऋ १६ ,य ३८ => 20*कला/201 => 60*कला/603
    नाडिका - 2*मुहुर्त,  # य १७ ऋ १६ ,य ३८
    द्युः - कला/603, #  ऋ १६ ,य ३८
    द्युः - मुहुर्त/30,  #  ऋ १६ ,य ३८

  # पंचत्रिंशं शतं पौष्णम् एकोनमयनोन्यृषेः। 
  # पर्वणां स्याच्चतुष्पादी काष्ठानां चैव ताः कलाः॥य ३०॥
    युग - चान्द्रायन/134, #(135-1) , # य ३०
    युग - पर्व/124, #(4*31) , # य ३०
    कला - काष्ठा/124, #(4*31) , # य ३०
    
  # द्युहेयं पर्व चेत्पादे पादस्त्रिंशत्तु सैकिका। 
  # भागात्मनापवृज्यांशान् निर्दिशेदधिको यदि॥य १२॥
     # पाद = 31
    द्युः - भागा/124, #य १२
    # अंश - भांश, 
    नक्षत्रम् -अंश_भांश/124,

  # ससप्तमं भयुक् सोमः सूर्यो द्यूनि त्रयोदश | 
  # नवमानि तु पञ्चाह्नः काष्ठा पञ्चाक्षरा भवेत् ॥य ३९॥
    गुर्वाक्षर - काष्ठा/5,

  # वसुस्त्वष्टा भवोऽजश्च मित्रः सर्पोऽश्विनौ जलम् | 
  # धाता कश्चायनाद्याः स्युरर्धपञ्चमभस्त्वृतुः ॥य १०॥
    सौरृतु - 2*नक्षत्रम्/9,

  # त्रिंशत्यह्नां सषट्षष्टिरब्दः षट् चर्तवोऽयने | 
  # मासा द्वादश सौर्याः स्युरेतत् पञ्चगुणं युगम् ॥य २८॥
    अब्दः - द्युः/366,
    अब्दः - सौरृतु/6,
    # अब्दः - सौर्मास/12,
    अब्दः - सौरायन/2,
    युग - अब्दः/5,

  # सावनेन्दुस्तृमासानां षष्टिः सैकद्विसप्तिका ।
  # द्युत्रिंशत् सावनस्याब्दः सौरः स्तॄणां स पर्ययः ॥य ३१ ॥
    युग - सौरमासः/61,
    युग - चान्द्रमासः/62,
    युग - स्तृमासः/67,

    नाडिका - minutes/24,
    hours - minutes/60,
    द्युः - hours/24,
    sym  -1
  ]), index=[str(sym)]).T
  display(ans.T)
  dfs.append((sym, ans))

sym, df = dfs[-1]
df = df.reset_index()
for _sym, _df in dfs[:-1] :
  print(_sym, df.shape, df['index'])
  df = pd.merge(df, _df.reset_index(), on="index")
  print(_sym, df.shape, df['index'])
  print("==============")

df =  df.set_index('index')
# df =df [ [str(x) for x in df.index] ]
df = df.sort_values(by='minutes')
df =df [ [str(x) for x in df.index] ]


# %%
from decimal import Decimal
# Decimal('1.25').as_integer_ratio()A
def fmtfrac(x):
  # ratio = Decimal(str(x)).as_integer_ratio()
  ratio = Decimal('%0.3f'%x).as_integer_ratio()
  if ( ratio[1] < 2000) : return ratio
  ratio = Decimal('%.03f' % (1/x) ).as_integer_ratio()
  return ( ratio[1], ratio[0])

# df1 = df.applymap( lambda x: Decimal(x).as_integer_ratio())
df1 = df.applymap(fmtfrac)
df2 = df.applymap( lambda x: re.sub("\.000$","",'%0.3f' %eval(str(x))))
display(df1, df2)

#%%
df1.to_csv("../datasets/vj-units-ratio.csv")
df2.to_csv("../datasets/vj-units-fractions.csv")


#%%
(hh, mm, d, m , y ) = symbols('hh mm d m y')
ans = solve([
  hh - mm/60,
  d - hh/24,
  m - d/30,
  y - m/12,
  d - 365
])
ans = pd.DataFrame(ans, index=['val']).T
ans['dec'] = ans.val.apply( lambda x: '%0.2f' %eval(str(x)))
ans

# %%
