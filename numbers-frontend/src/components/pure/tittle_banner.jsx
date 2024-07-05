import React, { } from "react";
import PropTypes from "prop-types";
import '../../static/style/bootstrap-5.1.1.min.css';
import '../../static/style/bootstrap.bundle.5.1.3.min.js'
import '../../static/style/style.css';

const TitleBanner = () => {

    return (
        <div className="m-0 title-banner">
            <div className='p-3'>
                <h1 className="fw-bolder">Numbers!</h1>
                <h4>Matemáticas Recreativas!</h4>
            </div>
        </div>
    );
}


TitleBanner.propTypes = {

};

export default TitleBanner;
