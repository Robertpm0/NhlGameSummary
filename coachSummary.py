import requests
import streamlit as st

st.set_page_config(layout="wide")
def TimeConvert(word):
    words=word.split(":")
    print(int(words[0])*60+int(words[1]))
    return int(words[0])*60+int(words[1])
    
#st.title("AVL @ DAL 5/15/2024")
st.markdown("<h1 style='text-align : center;' > AVL @ DAL 5/15/2024</h1>",unsafe_allow_html=True)
st.markdown("<h2 style='text-align : center;  ' > 2024 NHL Playoffs Game 5</h2>",unsafe_allow_html=True)
st.markdown("<h3 style='text-align : center;  ' > Final: 5 - 3</h3>",unsafe_allow_html=True)
st.markdown("<h6 style='text-align : center;  ' > SOG: 27 - 26</h6>",unsafe_allow_html=True)

st.markdown("---")
st.markdown("<h6 style='text-align : center;  ' > Goal Map - Time Line</h6>",unsafe_allow_html=True)
req=requests.get("https://api-web.nhle.com/v1/gamecenter/2023030235/play-by-play").json()
plays=req["plays"]
percentMap={1:[],2:[],3:[]}
win1=0
win2=0
per=1

currFoTime=0
dalFo=[]
colFo=[]
for play in plays:
    if play["typeDescKey"]=="goal":
        print(play)
        if play["details"]["eventOwnerTeamId"]==21:
            colFo.append(TimeConvert(play["timeInPeriod"])-TimeConvert(currFoTime))
        else:
            dalFo.append(TimeConvert(play["timeInPeriod"])-TimeConvert(currFoTime))


    elif play["typeDescKey"]=="faceoff":
        currFoTime=play["timeInPeriod"]

        if play["periodDescriptor"]["number"]>per:
            percentMap[per].append(win1)
            percentMap[per].append(win2)
            win1=win2=0
            per+=1 

        if play["details"]["eventOwnerTeamId"]==21:
            win1+=1
        else:
            win2+=1 
percentMap[per].append(win1)
percentMap[per].append(win2)

    
p1F0=round(percentMap[1][0]/(percentMap[1][0]+percentMap[1][1]),2)
p1F0b=round(1-p1F0,2)
p2F0=round(percentMap[2][0]/(percentMap[2][0]+percentMap[2][1]),2)
p2F0b=round(1-p2F0,2)
p3F0=round(percentMap[3][0]/(percentMap[3][0]+percentMap[3][1]),2)
p3F0b=1-p3F0

# '''
# req=requests.get("https://api-web.nhle.com/v1/gamecenter/2023030235/play-by-play").json()
# plays=req["plays"]
# goalX=[]
# goalY=[]
# goalPlayer=[]
# goalTeam=[]
# goalTimes=[]
# rawTimes=[]

# for play in plays:
#     if play["typeDescKey"]=="goal":
#         print(play)
#         goalX.append(play["details"]["xCoord"])
#         goalY.append(play["details"]["yCoord"])
#         goalTeam.append(play["details"]["eventOwnerTeamId"])
#         goalPlayer.append(play["details"]["scoringPlayerId"])
#         #if play["periodDescriptor"]["number"]>1:


#         goalTimes.append(TimeConvert(play["timeInPeriod"])+(( play["periodDescriptor"]["number"]-1)*TimeConvert("20:00")))
#         rawTimes.append(play["timeInPeriod"])

# #print(plays)
# #pd.read_json()


# #shots=(pd.read_parquet("https://github.com/sportsdataverse/fastRhockey-data/blob/main/nhl/pbp/parquet/play_by_play_2023.parquet?raw=true").query("event_type in ('GOAL')")
#     # 
# team_colors = {21: (0.59, 0,0), 25: (0, 0.7, 0.2)}

# teamMap = {21: "COL", 25: "DAL"}
# #teamMap = {22: "EDM", 23: "VAN"}

# #2023030235
# levels=[]

# for team in goalTeam:
#     if team==21:
#         levels.append(-1)
#     else:
#         levels.append(1)

# #2023030235




# #first_period = shots.query("game_id == 2022020001 and period == 1")
# #print(first_period.columns1)
# #print(first_period["x"])
# first_period=pd.DataFrame({"x":goalX,"y":goalY,"event_team":goalTeam})
# #https://api-web.nhle.com/v1/gamecenter/2023030235/play-by-play

# fig, axs = plt.subplots(1, 1, figsize=(2, 1))
# rink = NHLRink(

# )
# axs=rink.draw(ax=axs) 
# rink.scatter("x", "y", facecolor=first_period.event_team.map(team_colors), s=20, edgecolor="white", data=first_period, ax=axs)
# rink.plot_fn(sns.scatterplot, x="x", y="y", hue="event_team", s=20, legend=False, data=first_period, ax=axs, palette=team_colors)

# st.pyplot(plt)
# '''

dummyCol1,tcol2=st.columns(2)
with dummyCol1:
    st.image("rink.PNG")
with tcol2:

    st.image("cp.PNG")


st.markdown("---")
st.markdown("<h5 style='text-align : center;  ' >Team Analysis</h5>",unsafe_allow_html=True)
st.markdown("<h6 style='text-align : center;  ' >SAT Dif vs Hits per Player</h6>",unsafe_allow_html=True)

st.text("NOTE: Bubble Size = TOI \n Color = +/- \n SAT Dif = Shot Attempts For minus Shot Attempts Against")
#st.text("SAT Dif = Shot Attempts For minus Shot Attemps Against")
dummyCol1,tcol2=st.columns(2,gap="large")
with dummyCol1:
    st.markdown("<h4 style='text-align : center; color: maroon;' >COL</h4>",unsafe_allow_html=True) 
    st.image("colPlayers1.png")
with tcol2:
    st.markdown("<h4 style='text-align : center; color: green;' >DAL</h4>",unsafe_allow_html=True)
    st.image("dalPlayers1.png")



# '''
# fig,ax=plt.subplots(figsize=(2,1),layout="constrained")
# #plt.xticks([20*60,40*60],["2nd Per","3rd Per"])
# ax.set(title="Goal TImeline")
# ax.vlines(goalTimes,0,levels,color=[("tab:red" if tm ==21 else "tab:green")for tm in goalTeam])
# ax.axhline(0,c="black")

# for tme,lvl,tem,rt in zip(goalTimes,levels,goalTeam,rawTimes):
#     ax.annotate(f"{teamMap[tem]}@{rt}",xy=(tme,lvl),
#                 xytext=(-3,np.sign(lvl)*3),textcoords="offset points",
#                 verticalalignment="bottom"if lvl>0 else"top",weight="normal",
#                 bbox=dict(boxstyle="square",pad=0,lw=0,fc=(1,1,1,0.7)))
# ax.plot([20*60,40*60], np.zeros_like([20*60,40*60]), "ko", mfc="blue")    

# ax.xaxis.set_visible(False)
# ax.yaxis.set_visible(False)
# ax.spines[["left","top","right"]].set_visible(False)
# ax.margins(y=0.1)
# st.pyplot(plt)
# '''

st.markdown("<h3 style='text-align : center;  ' >Top Lines</h3>",unsafe_allow_html=True)
col1, col2 = st.columns(2,gap="small")
        #st.text("TOI  GF  GA  Shots  Blocks \n13:22 2  1    17       1")


with col1:

    st.markdown("<h4 style='text-align : center; color: maroon;' >COL</h4>",unsafe_allow_html=True)
    subCol1,subCol2=st.columns(2,gap="small")
    with subCol1:

      #  st.markdown("<h7 style='text-align : center;  ' >Forwards</h7>",unsafe_allow_html=True)
       # st.markdown("Drouin-Mackinnon-Lehkonen")
        #st.markdown("__TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks__   <br />      13:22 &nbsp; 2 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 17 &nbsp; &nbsp; &nbsp; &nbsp; 1",unsafe_allow_html=True)
        st.markdown("""
        <style>
        .column-border1 {
        border: 2px solid #000;
        border-radius: 5%;
        text-align: center;
        box-shadow: 1px 2px 20px maroon;
        }
        .dd {
                    text-indent: -10px;
        }
        .dd2 {
                    text-indent: -35px;
        }
        </style>
                    
        <div class='column-border1'>
            Forwards
                     <br />
            Drouin-Mackinnon-Lehkonen
                    <br />
                    <div class='dd'>
                    <strong>
             &nbsp;  TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks <br />
                    </strong>
                    </div>
                    <div class='dd2'>
            13:22 &nbsp; &nbsp; 2 &nbsp; &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 17 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1
                    </div>
        </div>
        """, unsafe_allow_html=True)
        #st.text("TOI  GF  GA  Shots  Blocks \n13:22 2  1    17       1")
      #  ColDf=pd.DataFrame({"TOI":["13:22"],"GF":[2],"GA":[1],"Shots":[17],"Blocks":[1]})
       # st.table(ColDf)
    with subCol2:
        #st.markdown("<h7 style='text-align : center;  ' >Defense</h7>",unsafe_allow_html=True)
        #st.markdown("Toews-Makar")
       # st.text("TOI  GF  GA  Blocks  Shots \n16:05 1  1    2       24")
       # st.markdown("__TOI &nbsp; &nbsp; GF  GA  Shots  Blocks__   <br />      16:05 &nbsp; 1 &nbsp;  1 &nbsp; &nbsp;  24 &nbsp; &nbsp; 2",unsafe_allow_html=True)

        #st.markdown("__TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks__   <br />      16:05 &nbsp; 1 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 24 &nbsp; &nbsp; &nbsp; &nbsp; 2",unsafe_allow_html=True)
        st.markdown("""
        <style>
        .column-border {
        border: 2px solid #000;
        border-radius: 5%;
        text-align: center;
        }
        .dd {
                    text-indent: -10px;
        }
        .dd2 {
                    text-indent: -35px;
        }
        </style>
                    
        <div class='column-border1'>
            Defenseman
                     <br />
           Toews-Makar
                    <br />
                    <div class='dd'>
                    <strong>
             &nbsp;  TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks <br />
                    </strong>
                    </div>
                    <div class='dd2'>
            16:05 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 24 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2
                    </div>
        </div>
        """, unsafe_allow_html=True)

with col2:

    st.markdown("<h4 style='text-align : center; color: green;' >DAL</h4>",unsafe_allow_html=True)

    subCol1,subCol2=st.columns(2,gap="small")
    with subCol1:
        #st.markdown("<h7 style='text-align : center;  ' >Forwards</h7>",unsafe_allow_html=True)
        #st.markdown("Drouin-Mackinnon-Lehkonen")
        #st.markdown("__TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks__   <br />      13:22 &nbsp; 2 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 17 &nbsp; &nbsp; &nbsp; &nbsp; 1",unsafe_allow_html=True)
        #st.text("TOI  GF  GA  Shots  Blocks \n13:22 2  1    17       1")
      #  ColDf=pd.DataFrame({"TOI":["13:22"],"GF":[2],"GA":[1],"Shots":[17],"Blocks":[1]})
       # st.table(ColDf)
        st.markdown("""
        <style>
        .column-border2 {
        border: 2px solid #000;
        border-radius: 5%;
        text-align: center;
        box-shadow: 1px 2px 20px lime;
        }
        .dd {
                    text-indent: -10px;
        }
        .dd2 {
                    text-indent: -35px;
        }
        </style>
                    
        <div class='column-border2'>
            Forwards
                     <br />
           Johnston-Benn-Stankoven
                    <br />
                    <div class='dd'>
                    <strong>
             &nbsp;  TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks <br />
                    </strong>
                    </div>
                    <div class='dd2'>
            10:52 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 0 &nbsp; &nbsp; &nbsp; 11 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 3
                    </div>
        </div>
        """, unsafe_allow_html=True)


    with subCol2:
       # st.markdown("<h7 style='text-align : center;  ' >Defense</h7>",unsafe_allow_html=True)
       # st.text("Toews-Makar")
       # st.text("TOI  GF  GA  Blocks  Shots \n16:05 1  1    2       24")
       # st.markdown("__TOI &nbsp; &nbsp; GF  GA  Shots  Blocks__   <br />      16:05 &nbsp; 1 &nbsp;  1 &nbsp; &nbsp;  24 &nbsp; &nbsp; 2",unsafe_allow_html=True)

        #st.markdown("__TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks__   <br />      16:05 &nbsp; 1 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 24 &nbsp; &nbsp; &nbsp; &nbsp; 2",unsafe_allow_html=True)
        #st.text("TOI  GF  GA  Shots  Blocks \n13:22 2  1    17       1")
        st.markdown("""
        <style>
        .column-border {
        border: 2px solid #000;
        border-radius: 5%;
        text-align: center;
        }
        .dd {
                    text-indent: -10px;
        }
        .dd2 {
                    text-indent: -35px;
        }
        </style>
                    
        <div class='column-border2'>
            Defenseman
                     <br />
           Lindell-Tanev
                    <br />
                    <div class='dd'>
                    <strong>
             &nbsp;  TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks <br />
                    </strong>
                    </div>
                    <div class='dd2'>
            9:20 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 7 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 5
                    </div>
        </div>
        """, unsafe_allow_html=True)


st.markdown("---")
st.markdown("<h3 style='text-align : center;  ' >Game Stats</h3>",unsafe_allow_html=True)
c1,c2,c3=st.columns([3,1,3])
with c1:
    st.markdown("<h5 style='text-align : center; color: maroon;' >COL</h5>",unsafe_allow_html=True)
    s1,s2,s3,s4=st.columns(4)
    with s1:
        st.markdown(f'''<p style='text-align : center;  ' ><strong>P1</strong></p> <br/> <p style='text-align : center;  ' >1</p> <br /> 
<p style='text-align : center;  ' >9</p>
<br />
<p style='text-align : center;  ' >13</p> <br />
    <p style='text-align : center;  ' >{p1F0}</p><br />
    <p style='text-align : center;  ' >3 </p><br />
    <p style='text-align : center;  ' > 3</p><br />
    <p style='text-align : center;  ' > 2</p>
                                        ''',
                    unsafe_allow_html=True)
    with s2:
        st.markdown(f'''<div style='border-left: 1px solid;'><p style='text-align : center;  ' ><strong>P2</strong></p> <br/> <p style='text-align : center;  ' >1</p> <br /> 
<p style='text-align : center;  ' >10</p>
<br />
<p style='text-align : center;  ' >16</p> <br />
    <p style='text-align : center;  ' >{p2F0}</p><br />
    <p style='text-align : center;  ' >2 </p><br />
    <p style='text-align : center;  ' > 2</p><br />
    <p style='text-align : center;  ' > 2</p></div>
                                        ''',
                    unsafe_allow_html=True)
       # Hits 16 ,block 3

    with s3:
        st.markdown(f'''<div style='border-left: 1px solid;'><p style='text-align : center;  ' ><strong>P3</strong></p> <br/> <p style='text-align : center;  ' >3</p> <br /> 
<p style='text-align : center;  ' >8</p>
<br />
<p style='text-align : center;  ' >7</p> <br />
    <p style='text-align : center;  ' >{p3F0}</p><br />
    <p style='text-align : center;  ' >5 </p><br />
    <p style='text-align : center;  ' > 1</p><br />
    <p style='text-align : center;  ' > 4</p></div>
                                        ''',
                    unsafe_allow_html=True)
# 7, blocks 5
    with s4:
        st.markdown(f'''<div style='border-left: 1px solid;'><p style='text-align : center;  ' ><strong>TOT</strong></p> <br/> <p style='text-align : center;  ' >5</p> <br /> 
<p style='text-align : center;  ' >27</p>
<br />
<p style='text-align : center;  ' >36</p> <br />
    <p style='text-align : center;  ' >0.45</p><br />
    <p style='text-align : center;  ' >10 </p><br />
    <p style='text-align : center;  ' > 6</p><br />
    <p style='text-align : center;  ' > 8</p></div>
                                        ''',
                    unsafe_allow_html=True)

with c2:
    st.markdown("<br />",unsafe_allow_html=True)

    st.markdown('''   
               
        <br />  <div style='border-right: 1px solid; border-left: 1px solid;'><p style='text-align : center; font-weight: bold; '></p><br/>
        <p style='text-align : center;font-weight: bold; border-bottom: 1px solid;' >  Goals </p><br/>
        <p style='text-align : center;font-weight: bold;border-bottom: 1px solid;' >Shots </p><br />
        <p style='text-align : center;font-weight: bold;border-bottom: 1px solid;' > Hits </p><br />
        <p style='text-align : center;font-weight: bold;border-bottom: 1px solid;' >Face Off %</p><br />
        <p style='text-align : center;font-weight: bold;border-bottom: 1px solid;' > Blocks </p><br />  
        <p style='text-align : center;font-weight: bold;border-bottom: 1px solid;' >Giveaways</p><br /> 
        <p style='text-align : center;font-weight: bold;' >Takeaways </p></div>''',unsafe_allow_html=True)


with c3:
    st.markdown("<h5 style='text-align : center; color: green;' >DAL</h5>",unsafe_allow_html=True)
    s1,s2,s3,s4=st.columns(4)
    with s1:
        st.markdown(f'''<p style='text-align : center;  ' ><strong>TOT</strong></p> <br/> <p style='text-align : center;  ' >3</p> <br /> 
<p style='text-align : center;  ' >26</p>
<br />
<p style='text-align : center;  ' >22</p> <br />
    <p style='text-align : center;  ' >0.55</p><br />
    <p style='text-align : center;  ' >17</p><br />
    <p style='text-align : center;  ' >7</p><br />
    <p style='text-align : center;  ' >10</p>
                                        ''',
                    unsafe_allow_html=True)
    with s2:
        st.markdown(f'''<div style='border-left: 1px solid;'><p style='text-align : center;  ' ><strong>P3</strong></p> <br/> <p style='text-align : center;  ' >1</p> <br /> 
<p style='text-align : center;  ' >10</p>
<br />
<p style='text-align : center;  ' >10</p> <br />
    <p style='text-align : center;  ' >{p3F0b}</p><br />
    <p style='text-align : center;  ' >7</p><br />
    <p style='text-align : center;  ' >3</p><br />
    <p style='text-align : center;  ' >2</p></div>
                                        ''',
                    unsafe_allow_html=True)
    with s3:
        st.markdown(f'''<div style='border-left: 1px solid;'><p style='text-align : center;  '> <strong>P2</strong></p> <br/> <p style='text-align : center;  ' >1</p> <br /> 
<p style='text-align : center;  ' >8</p>
<br />
<p style='text-align : center;  ' >8</p> <br />
    <p style='text-align : center;  ' >{p2F0b}</p><br />
    <p style='text-align : center;  ' >6 </p><br />
    <p style='text-align : center;  ' >2</p><br />
    <p style='text-align : center;  ' >5</p></div>
                                        ''',
                    unsafe_allow_html=True)        # 2 gives
    with s4:
        st.markdown(f'''<div style='border-left: 1px solid;'><p style='text-align : center;  ' ><strong>P1</strong></p> <br/> <p style='text-align : center;  ' >1</p> <br /> 
<p style='text-align : center;  ' >8</p>
<br />
<p style='text-align : center;  ' >4</p> <br />
    <p style='text-align : center;  ' >{p1F0b}</p><br />
    <p style='text-align : center;  ' >2</p><br />
    <p style='text-align : center;  ' >2</p><br />
    <p style='text-align : center;  ' >3</p></div>
                                        ''',
                    unsafe_allow_html=True)



st.markdown("---")
st.markdown("<h6 style='text-align : center;  ' >Misc Stats</h6>",unsafe_allow_html=True)

fc1,fc2,fc3,fc4=st.columns(4)


with fc1:

      #  st.markdown("<h7 style='text-align : center;  ' >Forwards</h7>",unsafe_allow_html=True)
       # st.markdown("Drouin-Mackinnon-Lehkonen")
        #st.markdown("__TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks__   <br />      13:22 &nbsp; 2 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 17 &nbsp; &nbsp; &nbsp; &nbsp; 1",unsafe_allow_html=True)
        st.markdown("""
        <style>
        .column-border {
        border: 2px solid #000;
        border-radius: 5%;
        text-align: center;
        }
        .dd {
                    text-indent: -10px;
        }
        .dd2 {
                    text-indent: -35px;
        }
        </style>
                    
        <div class='column-border'>
            Shot Attempts
                     <br />
                    <div class='dd'>
                    <strong>
           &nbsp; COL &nbsp; &nbsp &nbsp   &nbsp  &nbsp;  DAL <br />
                    </strong>
                    </div>
                    <div class='dd2'>
         &nbsp &nbsp   &nbsp &nbsp &nbsp 53 &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  45
                    </div>
        </div>
        """, unsafe_allow_html=True)
with fc2:

      #  st.markdown("<h7 style='text-align : center;  ' >Forwards</h7>",unsafe_allow_html=True)
       # st.markdown("Drouin-Mackinnon-Lehkonen")
        #st.markdown("__TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks__   <br />      13:22 &nbsp; 2 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 17 &nbsp; &nbsp; &nbsp; &nbsp; 1",unsafe_allow_html=True)
        st.markdown("""
        <style>
        .column-border {
        border: 2px solid #000;
        border-radius: 5%;
        text-align: center;
        }
        .dd {
                    text-indent: -10px;
        }
        .dd2 {
                    text-indent: -35px;
        }
        </style>
        """+f"""            
        <div class='column-border'>
            avg Seconds to Score After Faceoff
                     <br />
                    <div class='dd'>
                    <strong>
           &nbsp; COL &nbsp; &nbsp &nbsp   &nbsp  &nbsp;  DAL <br />
                    </strong>
                    </div>
                    <div class='dd2'>
         &nbsp &nbsp   &nbsp &nbsp &nbsp {round((sum(colFo)/len(colFo)),2)} &nbsp  &nbsp &nbsp &nbsp {round((sum(dalFo)/len(dalFo)),2)}
                    </div>
        </div>
        """, unsafe_allow_html=True)




with fc3:

      #  st.markdown("<h7 style='text-align : center;  ' >Forwards</h7>",unsafe_allow_html=True)
       # st.markdown("Drouin-Mackinnon-Lehkonen")
        #st.markdown("__TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks__   <br />      13:22 &nbsp; 2 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 17 &nbsp; &nbsp; &nbsp; &nbsp; 1",unsafe_allow_html=True)
        st.markdown("""
        <style>
        .column-border {
        border: 2px solid #000;
        border-radius: 5%;
        text-align: center;
        }
        .dd {
                    text-indent: -10px;
        }
        .dd2 {
                    text-indent: -35px;
        }
        </style>
                    
        <div class='column-border'>
            Power Play %
                     <br />
                    <div class='dd'>
                    <strong>
           &nbsp; COL &nbsp; &nbsp &nbsp   &nbsp  &nbsp;  DAL <br />
                    </strong>
                    </div>
                    <div class='dd2'>
         &nbsp &nbsp   &nbsp &nbsp &nbsp 2/3 &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  1/4
                    </div>
        </div>
        """, unsafe_allow_html=True)

with fc4:

      #  st.markdown("<h7 style='text-align : center;  ' >Forwards</h7>",unsafe_allow_html=True)
       # st.markdown("Drouin-Mackinnon-Lehkonen")
        #st.markdown("__TOI &nbsp; &nbsp; GF &nbsp; GA  &nbsp; Shots &nbsp;  Blocks__   <br />      13:22 &nbsp; 2 &nbsp; &nbsp; 1 &nbsp; &nbsp; &nbsp; 17 &nbsp; &nbsp; &nbsp; &nbsp; 1",unsafe_allow_html=True)
        st.markdown("""
        <style>
        .column-border {
        border: 2px solid #000;
        border-radius: 5%;
        text-align: center;
        box-shadow: 1px 2px 25px

        }
        .dd {
                    text-indent: -10px;
        }
        .dd2 {
                    text-indent: -35px;
        }
        </style>
                    
        <div class='column-border'>
            Power Play Shots (SOG - Attempts)
                     <br />
                    <div class='dd'>
                    <strong>
           &nbsp; COL &nbsp; &nbsp &nbsp   &nbsp  &nbsp;  DAL <br />
                    </strong>
                    </div>
                    <div class='dd2'>
         &nbsp &nbsp   &nbsp &nbsp &nbsp 2 - 6 &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  4 - 8
                    </div>
        </div>
        """, unsafe_allow_html=True)
        # htis 4,8, 10
        #blocks 7,6,4
#cum stats
#  Faceoffs
#  powerplay %
#     avg time after f0 goal



#df = px.data.gapminder()
