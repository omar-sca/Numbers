import React, { } from "react";
import PropTypes from "prop-types";
import '../../static/style/bootstrap-5.1.1.min.css';
import '../../static/style/bootstrap.bundle.5.1.3.min.js'
import '../../static/style/style.css';

const Spinner = () => {

    return (
        <div className="d-flex justify-content-center">
            <div className="spinner-border" role="status">
                <span className="visually-hidden">Loading...</span>
            </div>
        </div>
    );
}


Spinner.propTypes = {

};

export default Spinner;