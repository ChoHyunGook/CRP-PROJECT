import styles from "@/styles/Layout.module.css";
import {Header} from './Header'
import {Nav} from './Nav'
import {Table} from './Table'
import {Pagination} from './Pagination'
import {Footer} from './Footer'
import { Modal } from "./Modal";

export function Layout({ children }){
  return (
      <div className={styles.container}>
        <main className={styles.main}>{children}</main>
        <Table/>
        <Pagination/>
        <Modal/>
      </div>
  );
}