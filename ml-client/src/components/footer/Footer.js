import React from 'react';
import Github from '../../assets/images/dashboard/github.png'
import Donate from '../../assets/images/dashboard/donate.jpeg'
import Blog from '../../assets/images/dashboard/blog.png'
import Intagram from '../../assets/images/dashboard/Intagram.png'
import LinkedIn from '../../assets/images/dashboard/linkedin.png'
import Mobile from '../../assets/images/dashboard/mobile.jpeg'
import Hotmail from '../../assets/images/dashboard/hotmail.png'
import Gmail from '../../assets/images/dashboard/gmail.png'


const Footer = (props) => {
    return(
        <>
        <footer className='footer'>
            <div className='footer-content'>
                <h3>About</h3>
                <p>Founded in 2022, Apot Group look forward to sharing our experiences and interesting things in life that technology can do. The areas we are interested in at the moment are blockchain, AI, Analytics and Monitoring.</p>
            </div>
            <div className='footer-content'>
                <h3>Address</h3>
                <p>
                    876/67
                    CMT8
                    Tan Binh, Ho Chi Minh
                </p>
            </div>
            <div className='footer-content'>
                <h3>Contact</h3>
                <div className= 'footer-content-contact'>
                    <div className='fcl-item'>
                        <a href='tel:+84399360638'>
                            <img className="fcli-image" src={Mobile} alt=""></img>
                            +84 399 360 638
                        </a>
                    </div>
                    <div className='fcl-item'>
                        <a href='mailto:duynguyenngoc@hotmail.com'>
                            <img className="fcli-image" src={Hotmail} alt=""></img>
                            duynguyenngoc@hotmail.com
                        </a>
                    </div>
                    <div className='fcl-item'>
                        <a href='mailto:ngocduy.engineer@gmail.com'>
                            <img className="fcli-image" src={Gmail} alt=""></img>
                            ngocduy.engineer@gmail.com
                        </a>
                    </div>
                </div>
            </div>
            <div className='footer-content'>
                <h3>More Info</h3>
                <div className="footer-content-link">
                    <div className='fcl-item'>
                        <a href = 'https://github.com/dnguyenngoc'>
                            <img className="fcli-image" src={Github} alt=""></img>
                            Github
                        </a>
                    </div>
                    <div className='fcl-item'>
                        <a href = 'https://me.momo.vn/G9IwTNsRuZu2UAsNI4svUn'>
                            <img className="fcli-image" src={Donate} alt=""></img>
                            Donate
                        </a>
                    </div>
                    
                </div>
            </div>
            <div className='footer-content'>
                <h3>Follow us</h3>
                <div className="footer-content-link">
                    <div className='fcl-item'>
                        <a href = 'https://viblo.asia/u/dnguyenngoc'>
                            <img className="fcli-image" src={Blog} alt=""></img>
                            Blogs
                        </a>
                    </div>
                    <div className='fcl-item'>
                        <a href = 'https://www.linkedin.com/in/dnguyenngoc/'>
                            <img className="fcli-image" src={LinkedIn} alt=""></img>
                            LinkedIn
                        </a>
                    </div>
                    <div className='fcl-item'>
                        <a href = 'https://www.instagram.com/duy.nguyen.ngoc/'>
                            <img className="fcli-image" src={Intagram} alt=""></img>
                            Intagram
                        </a>
                    </div>
                </div>
            </div>
        </footer>
        </>
    ); 
}

export default Footer;