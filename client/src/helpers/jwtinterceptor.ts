import axios, {AxiosInstance} from "axios";
import { useNavigate } from "react-router-dom";
import { BASE_URL } from "../config";


const API_BASE_URL = BASE_URL


const useAxiosWIthInterceptor = (): AxiosInstance => {
    const jwtAxios = axios.create({baseURL : API_BASE_URL})
    const navigate = useNavigate()

    jwtAxios.interceptors.response.use(
        (response) => {
            return response
        }
    )
    return jwtAxios

}

export default useAxiosWIthInterceptor;