import { createError } from 'h3'

type ScoreRequestBody = {
  company_id: string
  dimensions: {
    governance: number
    innovation: number
    operations: number
    finance: number
    sustainability: number
  }
}

type FetchError = {
  response?: {
    status?: number
  }
  statusCode?: number
}

export default defineEventHandler(async (event) => {
  const { scoreServiceUrl } = useRuntimeConfig(event)
  const body = await readBody<ScoreRequestBody>(event)

  try {
    return await $fetch(`${scoreServiceUrl}/score`, {
      method: 'POST',
      body,
    })
  } catch (error: unknown) {
    const fetchError = error as FetchError
    const statusCode = fetchError.response?.status ?? fetchError.statusCode ?? 502

    throw createError({
      statusCode,
      message: 'Score service error',
    })
  }
})