import axios from 'axios'

import { ApiError } from '@/api/errors'

export const api = axios.create({
  baseURL: __API_URL__,
  headers: {
    'Content-Type': 'application/json',
  },
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (!error.response) throw new ApiError('Connection error')

    throw new ApiError(
      error.response.data?.detail ?? 'Unexpected response from the server',
      error.response.status,
    )
  },
)
