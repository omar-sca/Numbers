import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";
import { NumberKind } from "../../models/numberKind.class";
import { STATUS_REQUEST } from "../../models/statusRequest.enum";
import NumbersList from "./numbers_list";
import NumbersSetting from "./numbers_setting";
import { getNumbersListService } from "../../services/fetch_services";
import '../../static/style/bootstrap-5.1.1.min.css';
import '../../static/style/bootstrap.bundle.5.1.3.min.js'
import '../../static/style/style.css';
import InfoPopover from "./info";


const Accordion = ({ numberKindProps }) => {

	const [numbersList, setNumbersList] = useState([])
    const [statusRequest, setStatusRequest] = useState(null)

    useEffect(()=> {
        getNumbersListFunction();
        },[]);

    function getNumbersListFunction(amount=numberKindProps.min_len){
        getNumbersListService(numberKindProps.url_end_point, amount)
        .then((response) => {
            console.log("Numeros cargados OK")
            setNumbersList(JSON.parse(response.data));
            setStatusRequest(STATUS_REQUEST.SUCCESS)
        })
        .catch((response) => {
            console.log("Numeros cargados ERROR")
            setNumbersList([]);
            setStatusRequest(STATUS_REQUEST.ERROR)
        })
        .finally()
    }

    return (
        <div className="card-body">
            <div className="accordion-item">
                <h1 className="accordion-header" id={"panelsStayOpen-heading" + numberKindProps.id}>
                    <button className="accordion-button collapsed fw-bolder shadow-none" type="button" data-bs-toggle="collapse" data-bs-target={"#panelsStayOpen-collapse" + numberKindProps.id} aria-expanded="true" aria-controls={"panelsStayOpen-collapse" + numberKindProps.id}>
                        {numberKindProps.name}
                    </button>
                </h1>
                <div id={"panelsStayOpen-collapse" + numberKindProps.id} className="accordion-collapse collapse" aria-labelledby={"panelsStayOpen-heading" + numberKindProps.id}>
                    <div className="accordion-body">
                        <NumbersSetting props={ numberKindProps } onchangeFunction={getNumbersListFunction}></NumbersSetting>
                        <NumbersList n_list={ numbersList }></NumbersList>
                        <InfoPopover props={ numberKindProps }></InfoPopover>                     
                    </div>
                </div>
            </div>
        </div>

	);
}


Accordion.propTypes = {
	numberKindProps: PropTypes.instanceOf(NumberKind),
};

export default Accordion;
