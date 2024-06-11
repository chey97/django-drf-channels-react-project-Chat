import useAxiosWIthInterceptor from "../helpers/jwtinterceptor";
import { BASE_URL } from "../config";

const useCrud = () => {
    const jwtAxios = useAxiosWIthInterceptor();

    const fetchData = () => {
        // logic
    }
    
    return{fetchData}
}

export default useCrud;