import '../styles/globals.css'
import type { AppProps } from 'next/app'
import Footer from "@/components/common/Footer";
import {wrapper} from '@/modules/store'
import Nav  from '@/components/common/Nav'
import '../styles/index.css'
function MyApp({ Component, pageProps: {...pageProps} }: AppProps) {
  return ( 
    <>
    <Nav/>
    <Component {...pageProps} />
    <Footer/>
     <style jsx>{`
        a{
            textDecoration: none;
        }
    `}</style> 
    </>
  )
}

export default wrapper.withRedux(MyApp)
