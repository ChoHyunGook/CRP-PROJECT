import { ValidatorResponse, fileTypes } from '../types'

async function validateFileSize(fileSize: number): Promise<ValidatorResponse> {
    const documentFileSizeValidator = (await import('./fileSizeValidator')).default

    const validator = new documentFileSizeValidator(fileSize)
    const isValid = validator.validateFileSize()

    return {
        isValid,
        errorMessage: isValid ? '' : validator.getErrorMessage()
    }
}

async function validateFileType(fileType: string): Promise<ValidatorResponse> {
    const fileTypeValidator = (await import('./fileTypeValidator')).default

    const validator = new fileTypeValidator(fileType, fileTypes)
    const isValid = validator.validateFileType()

    return {
        isValid,
        errorMessage: isValid ? '' : validator.getErrorMessage()
    }
}

export default {
    validateFileSize,
    validateFileType
}