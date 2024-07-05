import React, { useEffect, useRef } from "react";
import PropTypes from "prop-types";
import { NumberKind } from "../../models/numberKind.class";
import imgInfo from "../../static/img/circle-info-light.svg"
import '../../static/style/bootstrap.bundle.5.1.3.min.js'
import '../../static/style/bootstrap-5.1.1.min.css';
import '../../static/style/style.css';

const InfoPopover = ({ props }) => {

    return (
        <div>
            <p className="d-flex justify-content-end">
                <button className="btn btn-white p-0 shadow-none" type="button" data-bs-toggle="collapse" data-bs-target={"#collapseExample" + props.id} aria-expanded="false" aria-controls={"collapseExample" + props.id}>
                    <img src={ imgInfo } className="logo" alt="Info" /> 
                </button>
            </p>
            <div className="collapse" id={"collapseExample" + props.id}>
                <div className="card card-body">
                    { props.description }
                </div>
            </div>
        </div>
    );
}


InfoPopover.propTypes = {
    props: PropTypes.instanceOf(NumberKind)
};

export default InfoPopover;
