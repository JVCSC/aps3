class ESGModel:
    def __init__(self):
        self.questions = self.generate_questions()
        self.responses = []

    def generate_questions(self):
        questions = [
            {"question": "A empresa possui políticas ambientais formalizadas?", "type": "yesno"},
            {"question": "A empresa utiliza materiais sustentáveis em seus projetos?", "type": "yesno"},
            {"question": "A empresa realiza avaliações de impacto ambiental antes de iniciar projetos?", "type": "yesno"},
            {"question": "Os funcionários recebem treinamento sobre práticas sustentáveis?", "type": "yesno"},
            {"question": "A empresa promove a diversidade e a inclusão no ambiente de trabalho?", "type": "yesno"},
            {"question": "A empresa possui programas de desenvolvimento comunitário?", "type": "yesno"},
            {"question": "A empresa mede suas emissões de gases de efeito estufa?", "type": "yesno"},
            {"question": "A empresa possui metas de redução de emissões?", "type": "yesno"},
            {"question": "A empresa investe em tecnologias para reduzir o impacto ambiental?", "type": "yesno"},
            {"question": "A empresa participa de iniciativas de responsabilidade social?", "type": "yesno"},
            {"question": "A empresa realiza auditorias independentes de suas práticas ESG?", "type": "yesno"},
            {"question": "A empresa publica relatórios de sustentabilidade?", "type": "yesno"},
            {"question": "A empresa possui certificações ambientais (ex: ISO 14001)?", "type": "yesno"},
            {"question": "A empresa realiza monitoramento contínuo da qualidade do ar nas obras?", "type": "yesno"},
            {"question": "A empresa adota práticas de construção sustentável?", "type": "yesno"},
            {"question": "A empresa possui programas de saúde e bem-estar para os funcionários?", "type": "yesno"},
            {"question": "A empresa está em conformidade com as regulamentações ambientais locais?", "type": "yesno"},
            {"question": "A empresa possui um plano de ação contra mudanças climáticas?", "type": "yesno"},
            {"question": "A empresa adota medidas para minimizar a poluição sonora?", "type": "yesno"},
            {"question": "A empresa promove a conscientização ambiental entre os stakeholders?", "type": "yesno"},
            {"question": "A empresa tem políticas contra o trabalho infantil e escravo?", "type": "yesno"},
            {"question": "A empresa tem iniciativas para reduzir o desperdício de materiais?", "type": "yesno"},
            {"question": "A empresa faz parcerias com ONGs ambientais?", "type": "yesno"},
            {"question": "A empresa possui práticas de gestão de água?", "type": "yesno"},
            {"question": "A empresa realiza avaliações periódicas de impacto social?", "type": "yesno"},
            {"question": "A empresa oferece estágios ou programas de formação para jovens?", "type": "yesno"},
            {"question": "A empresa tem uma política de compras sustentáveis?", "type": "yesno"},
            {"question": "A empresa promove a educação ambiental entre os funcionários?", "type": "yesno"},
            {"question": "A empresa tem um comitê de sustentabilidade?", "type": "yesno"},
            {"question": "A empresa realiza eventos ou campanhas de sustentabilidade?", "type": "yesno"},
            {"question": "A empresa incentiva o voluntariado entre os funcionários?", "type": "yesno"},
            {"question": "A empresa tem um programa de redução de carbono?", "type": "yesno"},
            {"question": "A empresa investe em pesquisa e desenvolvimento sustentável?", "type": "yesno"},
            {"question": "A empresa utiliza energias alternativas?", "type": "yesno"},
            {"question": "A empresa promove a igualdade de gênero?", "type": "yesno"},
            {"question": "A empresa adota práticas de transparência?", "type": "yesno"},
            {"question": "A empresa colabora com outras empresas para promover a sustentabilidade?", "type": "yesno"},
            {"question": "A empresa realiza avaliações de ciclo de vida dos produtos?", "type": "yesno"},
            {"question": "A empresa promove a reciclagem e reutilização de materiais?", "type": "yesno"},
            {"question": "A empresa tem uma estratégia de sustentabilidade de longo prazo?", "type": "yesno"},
        ]
        return questions

    def save_response(self, question_index, response):
        if 0 <= question_index < len(self.questions):
            self.responses.append({"question": self.questions[question_index]["question"], "response": response, "weight": self.questions[question_index]["weight"]})

    def calculate_results(self):
        total_score = 0.0
        for question, response in zip(self.questions, self.responses):
            if response["response"] == "Sim":
                total_score += question["weight"]
        
        return total_score
