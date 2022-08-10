import React from 'react';
import styles from "@/styles/Profile.module.css";
import style from '@/styles/Float.module.css'

const Profile: React.FC = () => {
return(
<>
<div className="col-md-3 text-center m-auto"> <br/><br/><br/>
    <h2>개발자 프로필</h2>
</div> <br/><br/><br/>
<div className='container h-100'>
<div className= "row d-flex justify-content-center align-items-center h-100">
<div className="card" style={{maxWidth: 20+"rem"}}>
<img src="https://ifh.cc/g/v681j8.jpg" width={"250px"} height={"400px"} className="card-img-top" alt="..."/>
    <div className="card-body">
        <h5 className="card-title">조현국</h5> <br/> 
        <p className="card-text">NLP <br/> KOBERT, KOGPT <br/> Pytorch, Tensorflow  <br/> Lyrics Software Developer</p>
        
    </div>
</div> &nbsp; &nbsp;

<div className="card" style={{maxWidth: 20+"rem"}}>
    <img src="https://ifh.cc/g/MGlTj5.jpg" width={"250px"} height={"400px"} className="card-img-top" alt="..."/>
        <div className="card-body">
            <h5 className="card-title">권혜민</h5> <br/> 
            <p className="card-text">CNN <br/>MuseGAN, Vision Transfomer<br/> Pytorch, Tensorflow <br/> Plagiarism, Analysis Software Developer </p>
            
        </div>
</div>
<div className="card" style={{maxWidth: 20+"rem"}}>
    <img src="https://ifh.cc/g/mRTjSh.jpg" width={"250px"} height={"400px"} className="card-img-top" alt="..."/>
        <div className="card-body">
            <h5 className="card-title">서성민</h5> <br/> 
            <p className="card-text"> TypeScript, JavaScript <br/> React, Next <br/> Redux , Redux Toolkit <br/> Composition Software Developer</p>
            
        </div>
</div>
</div>
</div>

<style jsx>{`
    .h2 {
        margin: 50px 0;
        
    }
`}</style>

</>)
}

export default Profile;