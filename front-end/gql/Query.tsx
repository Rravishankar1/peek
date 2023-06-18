import {gql} from "@apollo/client";
import { peekRequest } from "../protos/peek";


export const CONTINENT_QUERY = gql`
    query getNewData($request: peekRequest) {
        getCachedData(request: $request) {
        topics {
            name
            emoji
            highlight
            summary
            notifs {
            title
            uri
            }
        }
        }
    }
`;


export const NEW_DATA = gql`
    query getNewData($request: peekRequest) {
        getNewData(request: $request) {
        topics {
            name
            emoji
            highlight
            summary
            notifs {
            title
            uri
            }
        }
        }
    }
`;