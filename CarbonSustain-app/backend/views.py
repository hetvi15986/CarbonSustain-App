from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ActionSerializer
from .storage import load_actions, save_actions

class ActionList(APIView):
    def get(self, request):
        actions = load_actions()
        return Response(actions)

    def post(self, request):
        actions = load_actions()
        serializer = ActionSerializer(data=request.data)
        if serializer.is_valid():
            new_id = max([a["id"] for a in actions], default=0) + 1
            data = serializer.validated_data
            data["id"] = new_id
            actions.append(data)
            save_actions(actions)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActionDetail(APIView):
    def get_object(self, id):
        actions = load_actions()
        for action in actions:
            if action["id"] == id:
                return action, actions
        return None, actions

    def put(self, request, id):
        action, actions = self.get_object(id)
        if not action:
            return Response({"error": "Not found"}, status=404)
        serializer = ActionSerializer(data=request.data)
        if serializer.is_valid():
            updated = serializer.validated_data
            updated["id"] = id
            idx = next(i for i, a in enumerate(actions) if a["id"] == id)
            actions[idx] = updated
            save_actions(actions)
            return Response(updated)
        return Response(serializer.errors, status=400)

    def patch(self, request, id):
        action, actions = self.get_object(id)
        if not action:
            return Response({"error": "Not found"}, status=404)
        serializer = ActionSerializer(action, data=request.data, partial=True)
        if serializer.is_valid():
            updated = serializer.validated_data
            for k, v in updated.items():
                action[k] = v
            idx = next(i for i, a in enumerate(actions) if a["id"] == id)
            actions[idx] = action
            save_actions(actions)
            return Response(action)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        action, actions = self.get_object(id)
        if not action:
            return Response({"error": "Not found"}, status=404)
        actions = [a for a in actions if a["id"] != id]

