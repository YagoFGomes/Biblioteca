import React from 'react';
import './Main.css'
import Card from '../Card/Card';
import SideMenu from '../SideMenu/SideMenu';

const Main = () => {
    return (
        <div className='main'>
            <div className="row">
                <div className="column_1" >
                    <SideMenu />
                </div>
                <div className="column_2" >
                    <Card/>
                </div>
            </div>
        </div>
    );
};

export default Main;