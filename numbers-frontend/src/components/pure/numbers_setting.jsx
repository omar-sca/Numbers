import React, { useRef} from "react";
import PropTypes from "prop-types";
import { NumberKind } from "../../models/numberKind.class";
import '../../static/style/bootstrap-5.1.1.min.css';
import '../../static/style/bootstrap.bundle.5.1.3.min.js'


const NumbersSetting = ({ props, onchangeFunction }) => {

    const valueRef = useRef('')


    return (
        <div>
            <div className="">
                <p className="mb-0 text-center">Ingrese la cantidad de { props.is_serie ? "elementos de la" : "números" } {props.name} a mostar: </p>
                <div className="d-flex flex-wrap justify-content-center w-100">
                <input type="number" className="form-control w-25 text-center mt-2 mb-1" id={"inputNumber" + props.id} min={props.min_len} defaultValue={props.min_len} onChange={ ()=>onchangeFunction(valueRef.current.value) } ref={ valueRef }></input>
                </div>
            </div>
        </div>
    );
}


NumbersSetting.propTypes = {
    props: PropTypes.instanceOf(NumberKind)
};

export default NumbersSetting;

