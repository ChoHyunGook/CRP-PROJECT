import { Article } from "@/modules/types";
import axios, { AxiosResponse } from "axios";
import {HOST_4000} from "@/components/common/Path"

const headers = {
    "Content-Type" : "application/json",
    Authorization: "JWT fefege...",
} 
export class ArticleController {
    
    
    async writeArticle(writeData: Article) : Promise<any>  {
            try {
                await axios.post(`${HOST_4000}/Article`, writeData, {headers})            
            } catch (err) {
                return err;
            }
        }
    
    
    async removeArticle (id: any ) : Promise<any> {
        try{
            await axios.delete(`${HOST_4000}/Article/${id}`, {data : id} )
        } catch (err) {
            return(err);
        }
    }
    
    async writeComment (writeComment : Article) : Promise<any> {
        try{
            console.log('>>')
            await axios.post(`${HOST_4000}/Article`, writeComment, {headers})
        } catch (err){
            return(err)
        }
    }
    
    async readList ()  : Promise<any> {
        try{
            const response = await axios.get(`${HOST_4000}/Article`)
            return response.data
        } catch (err) {
            return(err)
        }
    }
    
 
}

