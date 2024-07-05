import React, { useState, useEffect } from "react";
import { getDashboardListService } from "../../services/fetch_services";
import { NumberKind } from "../../models/numberKind.class";
import { STATUS_REQUEST } from "../../models/statusRequest.enum";
import Accordion from "../pure/accordion";
import Spinner from "../pure/spiner";
import ErrorElement from "../pure/error_elem";
import '../../static/style/bootstrap-5.1.1.min.css';

const AccordionConteiner = () => {

    const [dashboardList, setDashboardList] = useState([],null)
    const [statusRequest, setStatusRequest] = useState(null)

    useEffect(() => {
        getDashboardListFunction()
    }, []);

    function getDashboardListFunction(){
        setStatusRequest(STATUS_REQUEST.LOADING)
        getDashboardListService()
            .then((response) => {
                console.log("Dashboard Exitoso!");
                let aux = [];
                response.data.map((e, i) => aux[i] = Object.assign(new NumberKind, e));
                setDashboardList(aux);
                setStatusRequest(STATUS_REQUEST.SUCCESS)
            })
            .catch((response) => {
                console.log("Dashboard Error!");
                setDashboardList([]);
                setStatusRequest(STATUS_REQUEST.ERROR)
            })
            .finally();
    }

    const SuccessComponent = () => {
        return (
            <div className="card" style={{ width: '30rem' }}>
                <div className="accordion" id="accordionPanelsStayOpenExample">
                    {
                        dashboardList.length > 0 ?
                            dashboardList.map((number, index) =>
                                <Accordion key={index} numberKindProps={number}></Accordion>)
                            :
                            <div className="text-center py-2">No hay números disponibles</div>
                    }
                </div>
            </div>
        )
    }


    return (
        <div>
            {
                statusRequest == STATUS_REQUEST.SUCCESS ?
                    <SuccessComponent></SuccessComponent>
                :
                    (
                        statusRequest == STATUS_REQUEST.ERROR ?
                            <ErrorElement func={ getDashboardListFunction }></ErrorElement>
                        : 
                            <Spinner></Spinner>
                    )
            }

        </div>
    );
}


AccordionConteiner.propTypes = {

};

export default AccordionConteiner;
