import { BACKEND_HOST } from "../../backend_config.enum";

export const getNumbersListService = async (end_point, amount)=> {
    let response = await fetch(BACKEND_HOST.URL_BASE + end_point + String(amount) + "/", {
        method: 'GET',
        });
    return response.json();
    };


export const getDashboardListService = async ()=> {
    let response = await fetch(BACKEND_HOST.URL_BASE, {
        method: 'GET',
        });
    return response.json();
    }
