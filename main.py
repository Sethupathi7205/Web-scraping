from bs4 import BeautifulSoup
import requests
import pandas as pd


Names= []
Price=[]
Desc= []



print(len(Names),len(Price),len(Desc))

try:
    url="https://www.airbnb.co.in/s/Chennai--India/homes?refinement_paths%5B%5D=%2Fhomes&place_id=ChIJYTN9T-plUjoRM9RjaAunYW4&location=Chennai%2C+India&checkin=&checkout="
    r= requests.get(url)


    soup= BeautifulSoup(r.text,"html.parser")
    #print(soup)
    for i in range(1,14):

        np=soup.find("a",class_="l1ovpqvx atm_1he2i46_1k8pnbi_10saat9 atm_yxpdqi_1pv6nv4_10saat9 atm_1a0hdzc_w1h1e8_10saat9 atm_2bu6ew_929bqk_10saat9 atm_12oyo1u_73u7pn_10saat9 atm_fiaz40_1etamxe_10saat9 c1ytbx3a atm_mk_h2mmj6 atm_9s_1txwivl atm_h_1h6ojuz atm_fc_1h6ojuz atm_bb_idpfg4 atm_26_1j28jx2 atm_3f_glywfm atm_7l_hkljqm atm_gi_idpfg4 atm_l8_idpfg4 atm_uc_10d7vwn atm_kd_glywfm atm_gz_8tjzot atm_uc_glywfm__1rrf6b5 atm_26_zbnr2t_1rqz0hn_uv4tnr atm_tr_kv3y6q_csw3t1 atm_26_zbnr2t_1ul2smo atm_3f_glywfm_jo46a5 atm_l8_idpfg4_jo46a5 atm_gi_idpfg4_jo46a5 atm_3f_glywfm_1icshfk atm_kd_glywfm_19774hq atm_70_glywfm_1w3cfyq atm_uc_aaiy6o_9xuho3 atm_70_18bflhl_9xuho3 atm_26_zbnr2t_9xuho3 atm_uc_glywfm_9xuho3_1rrf6b5 atm_70_glywfm_pfnrn2_1oszvuo atm_uc_aaiy6o_1buez3b_1oszvuo atm_70_18bflhl_1buez3b_1oszvuo atm_26_zbnr2t_1buez3b_1oszvuo atm_uc_glywfm_1buez3b_1o31aam atm_7l_1wxwdr3_1o5j5ji atm_9j_13gfvf7_1o5j5ji atm_26_1j28jx2_154oz7f atm_92_1yyfdc7_vmtskl atm_9s_1ulexfb_vmtskl atm_mk_stnw88_vmtskl atm_tk_1ssbidh_vmtskl atm_fq_1ssbidh_vmtskl atm_tr_pryxvc_vmtskl atm_vy_1vi7ecw_vmtskl atm_e2_1vi7ecw_vmtskl atm_5j_1ssbidh_vmtskl atm_mk_h2mmj6_1ko0jae dir dir-ltr").get("href")

        cnp="https://www.airbnb.co.in"+np
        #print(cnp)

        url= cnp
        r= requests.get(url)

        soup=BeautifulSoup(r.text,"html.parser")

        names =soup.find_all("div",class_="t1jojoys atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_1vgr820 atm_7l_jt7fhx atm_cs_10d11i2 atm_w4_1eetg7c atm_ks_zryt35__1rgatj2 dir dir-ltr")
        for name_tag in names:
            n=name_tag.text
            Names.append(n)
        price=soup.find_all("span",class_="u1y3vocb atm_7l_rb934l atm_cs_1peztlj dir dir-ltr")
        for price_tag in price:
            n=price_tag.text
            Price.append(n)

        disc=soup.find_all("span",class_="t6mzqp7 atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_kb7nvz atm_7l_1he744i atm_am_qk3dho atm_ks_zryt35__1rgatj2 dir dir-ltr")
        for disc_tag in disc:
            n=disc_tag.text
            Desc.append(n)

except Exception as e:
    print(e)

min_len=min(len(Names),len(Price),len(Desc),)
df=pd.DataFrame({"Hotel Name":Names[:min_len],"Price of the hotel":Price[:min_len],"stay_description":Desc[:min_len]})
df.to_csv("airbnb_chennai_stay1.csv")



























