import { apiClient } from "./client";
import { SearchResultItem } from "./types";

export async function globalSearch(query: string): Promise<SearchResultItem[]> {
  const { data } = await apiClient.get<{ query: string; results: SearchResultItem[] }>("/search/", {
    params: { q: query },
  });
  return data.results;
}
