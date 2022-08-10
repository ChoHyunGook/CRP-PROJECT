import '@/styles/globals.css'
import { Nav, Header, Layout, Footer} from '@/components'
import { wrapper } from '@/modules/store.js'
import styles from "@/styles/Header.module.css";
import withReduxSaga from 'next-redux-saga';
import PropTypes from "prop-types";

const App = ({ Component }) => {
  return  <>
  <Header/>
  <Nav/>
  <div className='AppMinHeight'>
    <Component/>
  </div>
  <Footer/>
  </>
}

App.propTypes = {
  Component: PropTypes.elementType,
};

export default wrapper.withRedux(withReduxSaga(App));

