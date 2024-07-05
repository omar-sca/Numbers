import React, { } from "react";
import PropTypes from "prop-types";
import reload_img from "../../static/img/reload_arrows.svg"
import '../../static/style/bootstrap-5.1.1.min.css';
import '../../static/style/bootstrap.bundle.5.1.3.min.js'
import '../../static/style/style.css';

const ErrorElement = ({func}) => {

    return (
        <div className="d-flex justify-content-center align-items-center">
                <p className="p-0 m-0 pe-1 fw-bolder">Error!</p>
                <button type="button" className="btn btn-outline-light p-0" onClick={ ()=>func() }>
                    <img src={ reload_img } className="logo" alt="Recargar" />   
                </button>
        </div>
    );
}


ErrorElement.propTypes = {

};

export default ErrorElement;