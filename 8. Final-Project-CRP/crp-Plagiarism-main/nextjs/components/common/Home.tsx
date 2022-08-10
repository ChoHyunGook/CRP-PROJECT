import css from "styled-jsx/css";
import { Button, Col, Form, Row } from "react-bootstrap";
import { useEffect } from "react";
import Link from "next/link";

const Home: React.FC = () => {
  const styled = css`
    .contents {
      height: 100%;
      margin: 10% 15%;
    }
    .wrapper {
      display: flex;
      justify-content: center;
      flex-direction: column;
    }
    .wrapper h1 {
      font-size: 40px;
    }
    .wrapper p {
      font-size: 20px;
    }
    .product0,
    .product1,
    .product2,
    .product3,
    .product4 {
      height: 500px;
      width: 100%;
      background-size: cover;
      background-repeat: no-repeat;
    }
    .product0 {
      background-size: 600px;
      background-position: 80% center;
      text-align: 40%;
    }
    .product1 p,
    .product3 p {
      text-align: right;
    }
    .product5 {
      text-align: center;
      margin: auto;
      margin-bottom: 10%;
    }
    .divButton {
      align-items: center;
    }
    .btn {
      font-size: 20px;
      padding: 15px 30px;
      background-color: white;
      color: rgb(51, 18, 110);
      border: 1px solid rgb(121, 91, 177);
      border-radius: 10px;
      letter-spacing: 4px;
      font-family: sans-serif;
      transition: all 0.4s;
    }
    .btn:focus {
      outline: none;
    }
    .btn:hover {
      border: rgb(121, 91, 177);
      background-color: rgb(121, 91, 177);
      color: white;
    }
  `;
  useEffect(() => {
    localStorage.clear();
  });

  return (
    <>
      <div
        id="Fade"
        className="carousel slide carousel-fade"
        data-bs-ride="carousel"
      >
        <div className="carousel-inner">
          <div className="carousel-item active" data-bs-interval="3000">
            <img
              src="/images/cutton.jpg"
              height={630}
              className="d-block w-100"
              alt="cutton"
            />
            <div className="carousel-caption text-start d-none d-md-block">
              <h2>Create Your Music</h2>
              <p>
                The music you hear is beautiful, but the music you do not hear
                is even more beautiful.
              </p>
            </div>
          </div>

          <div className="carousel-item" data-bs-interval="3000">
            <img
              src="/images/headset.jpg"
              height={630}
              className="d-block w-100"
              alt="piano"
            />
            <div className="carousel-caption text-end d-none d-md-block">
              <h1>Let me hear your music</h1>
              <p>The music that shines the most in the award is your music</p>
            </div>
          </div>
          <div className="carousel-item" data-bs-interval="3000">
            <img
              src="/images/band1.jpg"
              height={630}
              className="d-block w-100"
              alt="concert"
            />
            <div className="carousel-caption d-none d-md-block">
              <h1>Draw the world of your music</h1>
              <p>Music cleanses the dust of everyday life from the soul</p>
            </div>
          </div>
        </div>
      </div>
      <div className="contents">
        <section className="wrapper">
          <img
            src="/images/score.jpg"
            height={630}
            className="d-block w-100"
            alt="score"
          />{" "}
          <br />
          <br />
          <br />
          <br />
          <article className="product0">
            <h2>
              CRP만의 표절/작곡/작사 프로그램을 이용해보세요
              <br />
              <br />
              <Link href="/common/select">
                <a className="btn btn-secondary">바로가기 &raquo;</a>
              </Link>
            </h2>
          </article>
          <img
            src="/images/piano3.jpg"
            height={630}
            className="d-block w-100"
            alt="piano3"
          />{" "}
          <br />
          <br />
          <br />
          <br />
          <article className="product1">
            <h2>
              CRP만의 피아노로 자유롭게 연주해보세요
              <br />
              <br />
              <Link href="/piano/piano">
                <a className="btn btn-secondary">바로가기 &raquo;</a>
              </Link>
            </h2>
          </article>
          <img
            src="/images/search.jpg"
            height={630}
            className="d-block w-100"
            alt="search"
          />{" "}
          <br />
          <br />
          <br />
          <br />
          <article className="product2">
            <h2>CRP만의 뮤직 플레이어를 이용해보세요</h2>
            <br />
            <Link href="/music/player">
              <a className="btn btn-secondary">바로가기 &raquo;</a>
            </Link>
          </article>
          <div>
            <section className="mb-4">
              <h2 className="h1-responsive font-weight-bold text-center my-4">
                문의하기
              </h2>
              <p className="text-center w-responsive mx-auto mb-5">
                궁금한 사항은 문의를 주시면 친절하고 신속하게 답변 드리겠습니다.
              </p>
              <div className="row">
                <div className="col-md-3 text-center m-auto">
                  <ul className="list-unstyled mb-0 ">
                    <li>
                      <i className="fa fa-map-marker-alt fa"></i>
                      <p style={{ fontSize: 15 + "px" }}>
                        서울특별시 강남구 819 3 삼오빌딩 8층 803호
                      </p>
                    </li>
                    <li>
                      <i className="fa fa-phone mt-4 fa"></i>
                      <p>+ 01 234 567 89</p>
                    </li>
                    <li>
                      <i className="fa fa-envelope mt-4 fa"></i>
                      <p>crp.kr</p>
                    </li>
                  </ul>
                </div>
              </div>
            </section>
          </div>
        </section>
        <style jsx>{styled}</style>
      </div>
    </>
  );
};
export default Home;
