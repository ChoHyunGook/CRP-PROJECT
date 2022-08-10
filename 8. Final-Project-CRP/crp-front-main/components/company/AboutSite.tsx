import React from "react";
import style from '@/styles/Float.module.css'

const AboutSite: React.FC = () => {
    return(<>
        <div className="row">
          <div className="col-sm-4">
            <div className="card"> 
              <img src="https://ifh.cc/g/ZfTlKK.png" className="card-img-top" alt="악보나라" style={{width: 200+"px", margin: "0 auto"}}/>
              <div className="card-body">
                <h5 className="card-title">악보나라</h5> 
                <p className="card-text">피아노 악보, 기타, 베이스, 드럼 등 전문 악보 판매 사이트</p>
                <a href="https://www.akbonara.co.kr/" className="btn btn-dark">바로가기</a>
              </div>
            </div>
          </div>
          <div className="col-sm-4">
          <div className="card">
              <img src="https://cdn.loud.kr/prod/public/thumb/ORDER_SUB_22676_1_121113205154.jpg" className="card-img-top" alt="악보바다" style={{width: 200+"px", margin: "0 auto"}}/>
              <div className="card-body">
                <h5 className="card-title">악보바다</h5> 
                <p className="card-text">피아노 악보, 기타, 베이스, 드럼 등 전문 악보 판매 사이트</p>
                <a href="http://www.akbobada.com/" className="btn btn-dark">바로가기</a>
              </div>
            </div>
          </div>
          <div className="col-sm-4">
            <div className="card">
              <img src="https://www.youtube.com/img/desktop/yt_1200.png" className="card-img-top" alt="유튜브뮤직" style={{width: 225+"px", margin: "0 auto"}}/>
              <div className="card-body">
                <h5 className="card-title">유튜브뮤직</h5>
                <p className="card-text"> 음악 스트리밍 서비스</p>
                <a href="https://www.youtube.com/premium" className="btn btn-dark">바로가기</a>
              </div>
            </div>
          </div>
        </div><br/><br/>
        <div className="row">
          <div className="col-sm-4">
            <div className="card">
              <img src="https://play-lh.googleusercontent.com/GweSpOJ7p8RZ0lzMDr7sU0x5EtvbsAubkVjLY-chdyV6exnSUfl99Am0g8X0w_a2Qo4" className="card-img-top" alt="멜론" style={{width: 225+"px", margin: "0 auto"}}/>
              <div className="card-body">
                <h5 className="card-title">멜론</h5>
                <p className="card-text">음원판매 및 실시간 차트 확인 라이브 스트리밍</p>
                <a href="https://www.melon.com/" className="btn btn-dark">바로가기</a>
              </div>
            </div>
          </div>
          <div className="col-sm-4">
            <div className="card">
              <img src="https://img.hankyung.com/photo/202102/01.24077415.1-1200x.jpg" className="card-img-top" alt="Mnet" style={{width: 225+"px", margin: "0 auto"}}/>
              <div className="card-body">
                <h5 className="card-title">지니뮤직</h5>
                <p className="card-text">음원판매 및 실시간 차트 확인 라이브 스트리밍</p>
                <a href="https://www.genie.co.kr/buy/recommend?keywd=8EWgr627&source=adwords&gclid=Cj0KCQjw1tGUBhDXARIsAIJx01m6k3E6jsUCfSqdoZqKRl4qk3IJ3ixBaixlW-N8TUv4sQEVd43QAQ0aAqSQEALw_wcB" className="btn btn-dark">바로가기</a>
              </div>
            </div>
          </div>
          <div className="col-sm-4">
            <div className="card">
              <img src="http://www.sisanews.kr/news/photo/202004/47626_35000_1637.png" className="card-img-top" alt="뮤직카우" style={{width: 250+"px", margin: "0 auto"}}/>
              <div className="card-body">
                <h5 className="card-title">뮤직카우</h5>
                <p className="card-text">음악 저작권 플랫폼</p>
                <a href="https://www.musicow.com/about/bridge_a?utm_source=GDN&utm_medium=SA&utm_campaign=echomarketing_new_signup_web_search&utm_content=0_brand&utm_term=%EB%AE%A4%EC%A7%81%EC%B9%B4%EC%9A%B0&gclid=Cj0KCQjw1tGUBhDXARIsAIJx01njro7LIoM1SiQUM4cW9V1OX3SQ4I6UjBmATacZq7Gc84hsRl-Xi6UaAs05EALw_wcB" className="btn btn-dark">바로가기</a>
              </div>
            </div>
          </div>
        </div>
        
        </>)
}

export default AboutSite;