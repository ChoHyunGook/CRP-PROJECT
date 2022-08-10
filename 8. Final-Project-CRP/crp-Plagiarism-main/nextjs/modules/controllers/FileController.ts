import { UploadFileResponse } from "../types";
import { FileService } from "../services/FileService";
import { HOST_8000 } from "@/components/common/Path";
import axios from "axios";
export class FileController {
  private file: File;

  constructor(file: File) {
    this.file = file;
  }

  async uploadFile(): Promise<UploadFileResponse> {
    const fileService = new FileService();
    const uploadResponse = await axios.post(`http://127.0.0.1:8000/upload`, {
      method: "POST",
      body: fileService.getFormData(this.file),
    });

    //const responseJson = await uploadResponse.json();

    // if (responseJson.success === false) {
    //   return {
    //     success: false,
    //     message: responseJson.message,
    //   };
    // }

    return {
      success: true,
      message: "Uploaded Successfully",
    };
  }
}
