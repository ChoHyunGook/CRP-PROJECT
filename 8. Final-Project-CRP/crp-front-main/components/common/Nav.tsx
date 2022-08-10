import "bootstrap/dist/css/bootstrap.css";
import React, { useState } from "react";
import Link from "next/link";
import { HOST_3001, MUSIC_PLAYER_PORT } from "@/components/common/Path";

const Nav: React.FC = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light ">
      <div className="container-fluid">
        <Link href="/">
          <a className="navbar-brand">
            <img
              src="https://ifh.cc/g/KtohFH.png"
              style={{ width: 110 + "px" }}
              alt="logo"
            />
          </a>
        </Link>

        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0 m-auto">
            <li className="nav-item dropdown">
              <a
                className="nav-link dropdown-toggle  "
                href="#"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                회사소개
              </a>
              <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  {" "}
                  <Link href="/company/profile">
                    <a className="dropdown-item">개발자들</a>
                  </Link>
                </li>
                <li>
                  {" "}
                  <Link href="/company/oursite">
                    <a className="dropdown-item">사이트 소개</a>
                  </Link>
                </li>
              </ul>
            </li>

            <li className="nav-item dropdown">
              <a
                className="nav-link dropdown-toggle "
                href="#"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                게시판
              </a>
              <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  <Link href="/boards/addBoard">
                    <a className="dropdown-item">글쓰기</a>
                  </Link>
                </li>
                <li>
                  <Link  href="/boards/allBoardList">
                    <a className="dropdown-item">게시판 목록</a>
                  </Link>
                </li>
              </ul>
            </li>

            <li className="nav-item dropdown">
              <a
                className="nav-link dropdown-toggle "
                href="#"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                음악 프로그램
              </a>
              <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  <Link href="/piano/piano">
                    <a className="dropdown-item">피아노</a>
                  </Link>
                </li>
                <li>
                  <Link href="/music/player">
                    <a className="dropdown-item">뮤직 플레이어</a>
                  </Link>
                </li>
              </ul>
            </li>

            <ul className="nav-item">
              <li>
                <Link href="/common/select">
                  <a className="nav-link">표절/작곡/작사 프로그램</a>
                </Link>
              </li>
            </ul>

            <ul className="nav-item">
              <li>
                <Link href="/company/aboutSite">
                  <a className="nav-link ">관련 사이트</a>
                </Link>
              </li>
            </ul>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Nav;
