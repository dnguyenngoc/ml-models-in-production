import React from 'react';


const Footer = (props) => {
    return(
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
                    <a href='tel:+31202256153'>+84 399 360 638</a>
                    <a href='mailto:duynguyenngoc@hotmail.com'>duynguyenngoc@hotmail.com</a>
                    <a href='mailto:ngocduy.engineer@gmail.com'>ngocduy.engineer@gmail.com</a>
                </div>
            </div>
            <div className='footer-content'>
                <h3>Info</h3>
                <div className="footer-content-link">
                    <a href = '4'>Github</a>
                    <a href = '5'>Donate</a>
                </div>
            </div>
            <div className='footer-content'>
                <h3>Follow us</h3>
                <div className="footer-content-link">
                    <a href = '1'>Blogs</a>
                    <a href = '2'>Intagram</a>
                    <a href = '3'>LinkedIn</a>
                </div>
            </div>
        </footer>
    ); 
}

export default Footer;