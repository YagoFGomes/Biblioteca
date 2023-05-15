import React from 'react';
import './SideMenu.css'

const SideMenu = () => {
    return (
        <nav className="sidebar">

            <ul>
                <li><a href="#"><i className="icon icon-arrow-small-right"></i> Página Inícial</a></li>
                <li><a href="#"><i className="icon icon-arrow-small-right"></i> Códigos Html</a></li>
                <li><a href="#"><i className="icon icon-arrow-small-right"></i> Códigos Css</a></li>
                <li><a href="#"><i className="icon icon-arrow-small-right"></i> jQuery</a></li>
                <li><a href="#"><i className="icon icon-arrow-small-right"></i> WordPress</a></li>
            </ul>
    
        </nav>
    );
};

export default SideMenu;